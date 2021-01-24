# Generated by Django 2.2.3 on 2020-12-21 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_auto_20201221_1725'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useroperatelog',
            name='content',
            field=models.CharField(max_length=20, verbose_name='操作资产'),
        ),
        migrations.AlterField(
            model_name='useroperatelog',
            name='type',
            field=models.CharField(max_length=10, verbose_name='操作类型'),
        ),
        migrations.AlterField(
            model_name='useroperatelog',
            name='username',
            field=models.CharField(max_length=10, verbose_name='人员'),
        ),
    ]