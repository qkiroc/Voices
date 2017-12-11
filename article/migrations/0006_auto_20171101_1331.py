# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-01 13:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0005_img'),
    ]

    operations = [
        migrations.CreateModel(
            name='article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('article', models.TextField()),
                ('user', models.CharField(max_length=20)),
                ('liken', models.CharField(max_length=20)),
                ('commentn', models.CharField(max_length=20)),
                ('time', models.CharField(max_length=20)),
                ('solved', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('article', models.CharField(max_length=20)),
                ('user', models.CharField(max_length=20)),
                ('content', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='subcomment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('commnet', models.CharField(max_length=20)),
                ('user', models.CharField(max_length=20)),
                ('content', models.TextField()),
            ],
        ),
        migrations.RemoveField(
            model_name='user',
            name='article_id',
        ),
        migrations.AddField(
            model_name='user',
            name='img',
            field=models.CharField(default=2, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='user',
            name='head',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]
