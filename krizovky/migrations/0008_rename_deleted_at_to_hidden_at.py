from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("tajenky", "0007_add_soft_delete"),
    ]

    operations = [
        migrations.RenameField(
            model_name="crosswordanswer",
            old_name="deleted_at",
            new_name="hidden_at",
        ),
        migrations.RenameField(
            model_name="sourceurl",
            old_name="deleted_at",
            new_name="hidden_at",
        ),
    ]
