# Generated by Django 2.2.3 on 2020-11-12 12:39

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('asset', '0002_auto_20201112_1024'),
    ]

    operations = [
        migrations.CreateModel(
            name='Asset',
            fields=[
                ('asset_id', models.AutoField(primary_key=True, serialize=False, verbose_name='资产ID')),
                ('asset_name', models.CharField(max_length=64, null=True, verbose_name='资产名称')),
                ('asset_model', models.CharField(blank=True, max_length=32, verbose_name='型号')),
                ('specification', models.CharField(blank=True, max_length=256, verbose_name='规格参数')),
                ('department', models.CharField(blank=True, max_length=16, verbose_name='所属部门')),
                ('purchase_time', models.DateTimeField(blank=True, default=datetime.datetime.now, verbose_name='采购时间')),
                ('used_time', models.CharField(blank=True, max_length=64, verbose_name='使用年限')),
                ('asset_uuid', models.CharField(blank=True, max_length=128, unique=True, verbose_name='唯一标示')),
                ('comment', models.CharField(blank=True, max_length=512, verbose_name='备注')),
                ('modify_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='修改时间')),
                ('asset_holder', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '资产表',
                'verbose_name_plural': '资产表',
            },
        ),
        migrations.CreateModel(
            name='AssetHis',
            fields=[
                ('asset_id', models.AutoField(primary_key=True, serialize=False, verbose_name='资产ID')),
                ('asset_name', models.CharField(max_length=64, null=True, verbose_name='资产名称')),
                ('asset_model', models.CharField(blank=True, max_length=32, verbose_name='型号')),
                ('specification', models.CharField(blank=True, max_length=256, verbose_name='规格参数')),
                ('department', models.CharField(blank=True, max_length=16, verbose_name='所属部门')),
                ('purchase_time', models.DateTimeField(blank=True, default=datetime.datetime.now, verbose_name='采购时间')),
                ('used_time', models.CharField(blank=True, max_length=64, verbose_name='使用年限')),
                ('asset_uuid', models.CharField(blank=True, max_length=128, unique=True, verbose_name='唯一标示')),
                ('comment', models.CharField(blank=True, max_length=512, verbose_name='备注')),
                ('modify_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='修改时间')),
                ('asset_holder', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '资产历史表',
                'verbose_name_plural': '资产历史表',
            },
        ),
        migrations.RemoveField(
            model_name='server',
            name='asset_holder',
        ),
        migrations.RemoveField(
            model_name='server',
            name='asset_type',
        ),
        migrations.DeleteModel(
            name='ServerHis',
        ),
        migrations.RenameModel(
            old_name='ServerType',
            new_name='AssetType',
        ),
        migrations.DeleteModel(
            name='Server',
        ),
        migrations.AddField(
            model_name='asset',
            name='asset_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='asset.AssetType'),
        ),
    ]