# Generated by Django 4.0.4 on 2022-04-30 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0005_service_clinic_service_desc_service_specialist_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='desc',
            field=models.TextField(null=True),
        ),
    ]