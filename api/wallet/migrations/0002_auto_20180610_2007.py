# Generated by Django 2.0.6 on 2018-06-10 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wallet', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wallet',
            name='money',
            field=models.FloatField(default=0.0, verbose_name='钱包余额'),
        ),
    ]
