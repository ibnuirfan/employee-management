# Generated by Django 3.1.5 on 2021-01-25 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0006_appraisal_manager'),
    ]

    operations = [
        migrations.AddField(
            model_name='manager',
            name='manager_name',
            field=models.CharField(blank=True, max_length=25, verbose_name='Manager Name'),
        ),
    ]
