# Generated by Django 3.1 on 2022-03-22 05:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0032_auto_20201204_1229'),
    ]

    operations = [
        migrations.AlterField(
            model_name='macrogoal',
            name='daily_carbohydrates',
            field=models.IntegerField(default=None),
        ),
        migrations.AlterField(
            model_name='macrogoal',
            name='daily_fat',
            field=models.IntegerField(default=None),
        ),
        migrations.AlterField(
            model_name='macrogoal',
            name='daily_protein',
            field=models.IntegerField(default=None),
        ),
        migrations.AlterField(
            model_name='userconsumption',
            name='carbohydrates',
            field=models.IntegerField(default=datetime.date(2022, 3, 22)),
        ),
    ]
