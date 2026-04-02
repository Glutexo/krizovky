from django.db import migrations, models
import django.db.models.deletion


FALLBACK_SOURCE_URL = "https://neznamy-zdroj.invalid/"


def replace_fallback_source_url_with_null(apps, schema_editor):
    CrosswordAnswer = apps.get_model("tajenky", "CrosswordAnswer")
    SourceURL = apps.get_model("tajenky", "SourceURL")

    try:
        fallback_source_url = SourceURL.objects.get(url=FALLBACK_SOURCE_URL)
    except SourceURL.DoesNotExist:
        return

    CrosswordAnswer.objects.filter(source_url=fallback_source_url).update(source_url=None)

    if not fallback_source_url.answers.exists():
        fallback_source_url.delete()


class Migration(migrations.Migration):
    dependencies = [
        ("tajenky", "0005_rename_models_to_english"),
    ]

    operations = [
        migrations.AlterField(
            model_name="crosswordanswer",
            name="source_url",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="answers",
                to="tajenky.sourceurl",
                verbose_name="Zdrojová URL",
            ),
        ),
        migrations.RunPython(replace_fallback_source_url_with_null, migrations.RunPython.noop),
    ]
