# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-04 03:08
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0013_auto_20171102_1324'),
    ]

    operations = [
        migrations.RenameField(
            model_name='subcomment',
            old_name='commnet_id',
            new_name='comment_id',
        ),
    ]
