# Generated by Django 2.2.3 on 2020-12-28 12:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asset', '0017_auto_20201228_1239'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assetmaintance',
            name='date',
            field=models.DateField(blank=True, default=datetime.datetime.now),
        ),
    ]