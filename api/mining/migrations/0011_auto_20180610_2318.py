# Generated by Django 2.0.6 on 2018-06-10 23:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mining', '0010_auto_20180610_2155'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mining',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间'),
        ),
    ]