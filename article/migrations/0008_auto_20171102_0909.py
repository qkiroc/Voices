# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-02 09:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0007_delete_img'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='img',
        ),
        migrations.AddField(
            model_name='article',
            name='img',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]