# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-25 16:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goods',
            name='name',
            field=models.CharField(max_length=100, verbose_name='商品名'),
        ),
    ]
