# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-06-13 06:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('stocks', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BOSStock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.IntegerField(choices=[(0, '买'), (1, '卖')], default=0, verbose_name='买卖角色')),
                ('amount', models.IntegerField(null=True, verbose_name='数量')),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=8, verbose_name='价格')),
                ('datetime', models.DateTimeField(auto_now_add=True, verbose_name='时间')),
            ],
            options={
                'verbose_name': '挂单表',
                'verbose_name_plural': '挂单表',
            },
        ),
        migrations.CreateModel(
            name='DealStock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dealtime', models.DateTimeField(auto_now_add=True, verbose_name='交易时间')),
                ('stock', models.CharField(max_length=50, null=True, verbose_name='股票')),
                ('amount', models.IntegerField(null=True, verbose_name='数量')),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=8, null=True, verbose_name='价格')),
            ],
            options={
                'verbose_name': '记录表',
                'verbose_name_plural': '记录表',
            },
        ),
        migrations.CreateModel(
            name='SelfStock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stock', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stocks.Stock', verbose_name='股票')),
            ],
            options={
                'verbose_name': '自选股票表',
                'verbose_name_plural': '自选股票表',
            },
        ),
    ]
