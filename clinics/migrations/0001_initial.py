# Generated by Django 4.0.4 on 2022-04-29 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Clinic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, null=True)),
                ('phone_num', models.CharField(max_length=15, null=True)),
                ('region', models.CharField(max_length=250, null=True)),
                ('district', models.CharField(max_length=250, null=True)),
                ('street', models.CharField(max_length=250, null=True)),
                ('home_num', models.CharField(max_length=15, null=True)),
                ('open_time', models.TimeField()),
                ('close_time', models.TimeField()),
            ],
        ),
    ]
