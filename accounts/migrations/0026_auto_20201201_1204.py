# Generated by Django 3.1.3 on 2020-12-01 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0025_auto_20201201_1153'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userconsumption',
            name='datestamp',
            field=models.DateField(),
        ),
    ]
