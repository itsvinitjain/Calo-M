# Generated by Django 3.1.3 on 2020-12-02 16:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0029_auto_20201201_1507'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userconsumption',
            name='carbohydrates',
            field=models.IntegerField(default=datetime.date(2020, 12, 2)),
        ),
    ]