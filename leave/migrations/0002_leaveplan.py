# Generated by Django 3.0.7 on 2020-08-06 09:12

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0002_employee_bonus'),
        ('leave', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='LeavePlan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('plan_date', models.DateField(default=django.utils.timezone.now)),
                ('approval_status', models.BooleanField(default=False)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employees.Employee')),
            ],
        ),
    ]
