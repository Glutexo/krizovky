from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("tajenky", "0004_split_source_url_model"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="ZdrojovaURL",
            new_name="SourceURL",
        ),
        migrations.RenameModel(
            old_name="Tajenka",
            new_name="CrosswordAnswer",
        ),
        migrations.RenameField(
            model_name="crosswordanswer",
            old_name="source",
            new_name="source_url",
        ),
        migrations.AlterModelTable(
            name="sourceurl",
            table="crossword_answers_source_url",
        ),
        migrations.AlterModelTable(
            name="crosswordanswer",
            table="crossword_answers_crossword_answer",
        ),
        migrations.AlterField(
            model_name="crosswordanswer",
            name="source_url",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                related_name="answers",
                to="tajenky.sourceurl",
                verbose_name="Zdrojová URL",
            ),
        ),
    ]
