# Generated by Django 3.2.7 on 2021-09-20 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BRMapp', '0004_rename_wanted_applier_expect'),
    ]

    operations = [
        migrations.AddField(
            model_name='applier',
            name='position',
            field=models.TextField(default=''),
        ),
    ]
