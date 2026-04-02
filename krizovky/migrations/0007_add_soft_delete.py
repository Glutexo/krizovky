from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("tajenky", "0006_make_source_url_optional"),
    ]

    operations = [
        migrations.AddField(
            model_name="crosswordanswer",
            name="deleted_at",
            field=models.DateTimeField(blank=True, null=True, verbose_name="Smazáno"),
        ),
        migrations.AddField(
            model_name="sourceurl",
            name="deleted_at",
            field=models.DateTimeField(blank=True, null=True, verbose_name="Smazáno"),
        ),
    ]
