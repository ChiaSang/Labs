# Generated by Django 2.2.3 on 2020-11-16 19:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('asset', '0004_auto_20201114_2230'),
    ]

    operations = [
        migrations.CreateModel(
            name='AssetStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('asset_status', models.CharField(max_length=16, verbose_name='资产状态')),
            ],
            options={
                'verbose_name': '资产状态表',
                'verbose_name_plural': '资产状态表',
            },
        ),
        migrations.AlterField(
            model_name='asset',
            name='asset_uuid',
            field=models.CharField(blank=True, max_length=128, null=True, unique=True, verbose_name='唯一标示'),
        ),
        migrations.AddField(
            model_name='asset',
            name='asset_status',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='asset.AssetStatus'),
        ),
    ]