# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-06-13 07:21
from __future__ import unicode_literals

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
        ('stocks', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=30, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('mobile', models.CharField(blank=True, max_length=11, null=True, unique=True, verbose_name='手机号码')),
                ('email', models.CharField(blank=True, max_length=30, null=True, verbose_name='邮箱')),
                ('identity', models.CharField(blank=True, max_length=20, null=True, verbose_name='身份证号')),
                ('isactive', models.BooleanField(default=False, verbose_name='是否激活')),
                ('isban', models.BooleanField(default=False, verbose_name='是否禁用')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': '用户信息',
                'verbose_name_plural': '用户信息',
                'db_table': 'User',
                'ordering': ['-id'],
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Bank',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=40, verbose_name='持卡人姓名')),
                ('bank', models.CharField(choices=[(0, '中国银行'), (1, '工商银行'), (2, '建设银行'), (3, '农业银行'), (4, '交通银行'), (5, '招商银行')], default=0, max_length=40, verbose_name='开户行')),
                ('bankNo', models.CharField(max_length=40, verbose_name='卡号')),
                ('tradepwd', models.CharField(max_length=100, verbose_name='交易密码')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='用户')),
            ],
            options={
                'verbose_name': '银行表',
                'verbose_name_plural': '银行表',
                'db_table': 'Bank',
            },
        ),
        migrations.CreateModel(
            name='Fund',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('money', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True, verbose_name='总资金')),
                ('frozen_money', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True, verbose_name='冻结资金')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='用户')),
            ],
            options={
                'verbose_name': '资金表',
                'verbose_name_plural': '资金表',
                'db_table': 'Fund',
            },
        ),
        migrations.CreateModel(
            name='Hold',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField(blank=True, null=True, verbose_name='持有数量')),
                ('frozen', models.IntegerField(blank=True, null=True, verbose_name='冻结股')),
                ('stock', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stocks.Stock', verbose_name='股票')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='用户')),
            ],
            options={
                'verbose_name': '持仓表',
                'verbose_name_plural': '持仓表',
                'db_table': 'Hold',
            },
        ),
    ]
