# Generated by Django 2.2.1 on 2019-07-12 07:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0022_auto_20190712_1012'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teams',
            name='jst',
        ),
        migrations.AlterField(
            model_name='employee',
            name='position',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='employees.Job_Titles'),
        ),
    ]
