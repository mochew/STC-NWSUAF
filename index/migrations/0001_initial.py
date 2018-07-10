# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-07-09 16:21
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Admirelog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isGood', models.BooleanField(default=True)),
                ('isFile', models.BooleanField(default=True)),
                ('create_time', models.DateTimeField(default=datetime.datetime.now)),
                ('aid', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='chat.Article')),
            ],
            options={
                'verbose_name_plural': '点赞表',
                'verbose_name': '点赞表',
                'ordering': ['create_time'],
            },
        ),
        migrations.CreateModel(
            name='Colleges',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('desc', models.TextField()),
                ('picture', models.ImageField(null=True, upload_to='')),
            ],
            options={
                'verbose_name_plural': '学院/文件类型',
                'verbose_name': '学院/文件类型',
            },
        ),
        migrations.CreateModel(
            name='Collegetype',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('desc', models.TextField()),
            ],
            options={
                'verbose_name_plural': '学院类型',
                'verbose_name': '学院类型',
            },
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(default=datetime.datetime.now)),
                ('content', models.CharField(max_length=1000)),
                ('have_read', models.BooleanField(default=False)),
                ('arg0', models.IntegerField(null=True)),
                ('arg1', models.IntegerField(null=True)),
                ('arg2', models.IntegerField(null=True)),
                ('arg3', models.IntegerField(null=True)),
            ],
            options={
                'verbose_name_plural': '全局通知',
                'verbose_name': '全局通知',
                'ordering': ['create_time'],
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=100)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('create_time', models.DateTimeField(default=datetime.datetime.now)),
                ('profile_photo', models.ImageField(blank=True, default='static/img/logo.png', upload_to='static/upload/profile_photo')),
                ('degree_good', models.FloatField(default=0)),
                ('good_mark', models.IntegerField(default=0)),
                ('bad_mark', models.IntegerField(default=0)),
                ('trade_count', models.IntegerField(default=0)),
            ],
            options={
                'verbose_name_plural': '用户',
                'verbose_name': '用户',
                'ordering': ['create_time'],
            },
        ),
        migrations.AddField(
            model_name='notification',
            name='aim_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='aim_user', to='index.User'),
        ),
        migrations.AddField(
            model_name='notification',
            name='arg4',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='index.User'),
        ),
        migrations.AddField(
            model_name='colleges',
            name='classify',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='index.Collegetype'),
        ),
    ]
