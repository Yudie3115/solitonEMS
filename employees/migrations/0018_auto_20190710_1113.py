# Generated by Django 2.2.1 on 2019-07-10 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0017_auto_20190710_0954'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teams',
            name='status',
            field=models.CharField(default='Active', max_length=15),
        ),
    ]
