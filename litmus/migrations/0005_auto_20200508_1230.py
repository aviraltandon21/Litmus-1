# Generated by Django 3.0.4 on 2020-05-08 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('litmus', '0004_notes'),
    ]

    operations = [
        migrations.RenameField(
            model_name='notes',
            old_name='diary_notes',
            new_name='note_body',
        ),
        migrations.AddField(
            model_name='notes',
            name='note_title',
            field=models.TextField(default='Title'),
        ),
    ]