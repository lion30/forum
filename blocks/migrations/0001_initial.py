# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-22 12:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Block',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='模块名称')),
                ('desc', models.CharField(max_length=100, verbose_name='模块描述')),
                ('manager_name', models.CharField(max_length=100, verbose_name='模块管理员名称')),
            ],
        ),
    ]
