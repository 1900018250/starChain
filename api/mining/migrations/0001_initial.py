# Generated by Django 2.0.6 on 2018-06-10 15:08

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('wallet', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mining',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('force', models.IntegerField(verbose_name='矿机算力')),
                ('add_time', models.DateTimeField(default=datetime.datetime(2018, 6, 10, 15, 8, 20, 702429), verbose_name='添加时间')),
                ('extract', models.FloatField(verbose_name='已经被取到钱包的矿石')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='所属用户')),
                ('wallet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wallet.Wallet', verbose_name='所属钱包')),
            ],
            options={
                'verbose_name': '矿机信息',
                'verbose_name_plural': '矿机信息',
            },
        ),
    ]