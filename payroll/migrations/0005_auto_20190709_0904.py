# Generated by Django 2.2.2 on 2019-07-09 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payroll', '0004_auto_20190709_0643'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payroll',
            name='bonus',
            field=models.CharField(default='0.0', max_length=20),
        ),
        migrations.AlterField(
            model_name='payroll',
            name='damage_deduction',
            field=models.CharField(default='0.0', max_length=20),
        ),
        migrations.AlterField(
            model_name='payroll',
            name='overtime',
            field=models.CharField(default='0.0', max_length=20),
        ),
        migrations.AlterField(
            model_name='payroll',
            name='prorate',
            field=models.CharField(default='0.0', max_length=20),
        ),
        migrations.AlterField(
            model_name='payroll',
            name='sacco_deduction',
            field=models.CharField(default='0.0', max_length=20),
        ),
    ]
