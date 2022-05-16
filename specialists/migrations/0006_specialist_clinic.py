# Generated by Django 4.0.4 on 2022-05-13 12:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clinics', '0003_clinic_image'),
        ('specialists', '0005_alter_specialist_education'),
    ]

    operations = [
        migrations.AddField(
            model_name='specialist',
            name='clinic',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='clinics.clinic'),
            preserve_default=False,
        ),
    ]