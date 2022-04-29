# Generated by Django 4.0.4 on 2022-04-29 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=250, null=True)),
                ('medical_card', models.CharField(max_length=200, null=True)),
                ('contact', models.CharField(max_length=15, null=True)),
                ('address', models.CharField(max_length=350, null=True)),
            ],
        ),
    ]