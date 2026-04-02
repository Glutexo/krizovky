from django.db import migrations, models
import django.db.models.deletion


FALLBACK_SOURCE_URL = "https://neznamy-zdroj.invalid/"


def move_source_urls_to_parent_model(apps, schema_editor):
    Tajenka = apps.get_model("tajenky", "Tajenka")
    ZdrojovaURL = apps.get_model("tajenky", "ZdrojovaURL")

    fallback_source, _ = ZdrojovaURL.objects.get_or_create(url=FALLBACK_SOURCE_URL)

    for tajenka in Tajenka.objects.all():
        if tajenka.source_url:
            source, _ = ZdrojovaURL.objects.get_or_create(url=tajenka.source_url)
        else:
            source = fallback_source

        tajenka.source_id = source.id
        tajenka.save(update_fields=["source"])


class Migration(migrations.Migration):
    dependencies = [
        ("tajenky", "0003_tajenka_source_url"),
    ]

    operations = [
        migrations.CreateModel(
            name="ZdrojovaURL",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("url", models.URLField(unique=True, verbose_name="Zdrojová URL")),
                ("created_at", models.DateTimeField(auto_now_add=True, verbose_name="Vytvořeno")),
                ("updated_at", models.DateTimeField(auto_now=True, verbose_name="Upraveno")),
            ],
            options={
                "verbose_name": "zdrojová URL",
                "verbose_name_plural": "zdrojové URL",
                "ordering": ["url"],
            },
        ),
        migrations.AddField(
            model_name="tajenka",
            name="source",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="tajenky",
                to="tajenky.zdrojovaurl",
                verbose_name="Zdrojová URL",
            ),
        ),
        migrations.RunPython(move_source_urls_to_parent_model, migrations.RunPython.noop),
        migrations.AlterField(
            model_name="tajenka",
            name="source",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                related_name="tajenky",
                to="tajenky.zdrojovaurl",
                verbose_name="Zdrojová URL",
            ),
        ),
        migrations.RemoveField(
            model_name="tajenka",
            name="source_url",
        ),
    ]
