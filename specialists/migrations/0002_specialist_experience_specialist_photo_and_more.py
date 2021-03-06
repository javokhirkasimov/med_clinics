# Generated by Django 4.0.4 on 2022-04-30 01:41

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('specialists', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='specialist',
            name='experience',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='specialist',
            name='photo',
            field=models.ImageField(null=True, upload_to='specialist_photo'),
        ),
        migrations.AddField(
            model_name='specialist',
            name='skills',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=255), null=True, size=10),
        ),
    ]
