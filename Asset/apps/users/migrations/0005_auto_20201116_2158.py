# Generated by Django 2.2.3 on 2020-11-16 21:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20201116_2133'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='department',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.Department'),
        ),
    ]
