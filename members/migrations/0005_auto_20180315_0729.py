# Generated by Django 2.0.3 on 2018-03-15 01:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0004_auto_20180314_2346'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='mobile_number',
            field=models.IntegerField(unique=True),
        ),
    ]
