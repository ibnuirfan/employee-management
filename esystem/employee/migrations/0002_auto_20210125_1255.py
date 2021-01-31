# Generated by Django 3.1.5 on 2021-01-25 12:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='appraisal',
            options={'verbose_name_plural': 'Appraisals'},
        ),
        migrations.AddField(
            model_name='appraisal',
            name='department',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='employee.department'),
        ),
        migrations.AddField(
            model_name='appraisal',
            name='employee',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='employee.employee'),
        ),
        migrations.AddField(
            model_name='appraisal',
            name='manager',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='employee.manager'),
        ),
        migrations.AddField(
            model_name='employee',
            name='manager',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='employee.manager'),
        ),
    ]