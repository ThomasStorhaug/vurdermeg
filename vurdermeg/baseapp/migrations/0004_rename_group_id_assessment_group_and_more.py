# Generated by Django 4.1.5 on 2023-01-19 11:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("baseapp", "0003_rename_answer_text_answer_data_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="assessment",
            old_name="group_id",
            new_name="group",
        ),
        migrations.RenameField(
            model_name="assessmentgroup",
            old_name="group_name",
            new_name="name",
        ),
        migrations.RenameField(
            model_name="tag",
            old_name="tag_name",
            new_name="name",
        ),
    ]