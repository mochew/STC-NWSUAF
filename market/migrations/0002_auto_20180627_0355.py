# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-06-27 03:55
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0001_initial'),
        ('market', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Evidence',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(default=datetime.datetime.now)),
                ('content', models.ImageField(blank=True, default='', upload_to='static/upload/evidence')),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='index.User')),
            ],
            options={
                'ordering': ['create_time'],
                'verbose_name': '证据',
                'verbose_name_plural': '证据',
            },
        ),
        migrations.AlterModelOptions(
            name='feedback',
            options={'ordering': ['create_time'], 'verbose_name': '投诉', 'verbose_name_plural': '投诉'},
        ),
        migrations.AddField(
            model_name='feedback',
            name='create_time',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='feedback',
            name='creator',
            field=models.ForeignKey(default=1111, on_delete=django.db.models.deletion.CASCADE, to='index.User'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='feedback',
            name='info',
            field=models.CharField(default=1111, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='feedback',
            name='is_ongoing',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='evidence',
            name='feedback',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='market.Feedback'),
        ),
    ]
