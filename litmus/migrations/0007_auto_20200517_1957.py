# Generated by Django 3.0.4 on 2020-05-17 14:27

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('litmus', '0006_auto_20200517_1944'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notes',
            name='create_time',
        ),
        migrations.AddField(
            model_name='notes',
            name='create_date',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
