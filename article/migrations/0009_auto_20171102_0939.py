# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-02 09:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0008_auto_20171102_0909'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='user2',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='comment',
            name='user2_id',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='comment',
            name='user_id',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='subcomment',
            name='user2',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='subcomment',
            name='user2_id',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='subcomment',
            name='user_id',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
    ]
