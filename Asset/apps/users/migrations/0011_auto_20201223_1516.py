# Generated by Django 2.2.3 on 2020-12-23 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_auto_20201221_2031'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='dp_name',
            field=models.CharField(default='默认', max_length=8, verbose_name='部门'),
        ),
    ]