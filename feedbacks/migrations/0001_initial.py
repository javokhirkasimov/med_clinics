# Generated by Django 4.0.4 on 2022-04-30 03:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('specialists', '0005_alter_specialist_education'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=250, null=True)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('message', models.TextField(null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('specialist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='specialists.specialist')),
            ],
        ),
    ]
