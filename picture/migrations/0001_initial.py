# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=32, verbose_name='\u540d\u79f0', db_index=True)),
            ],
            options={
                'db_table': 'category',
                'verbose_name': '\u5206\u7c7b',
                'verbose_name_plural': '\u5206\u7c7b',
            },
        ),
        migrations.CreateModel(
            name='CP',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=32, verbose_name='\u540d\u79f0', db_index=True)),
            ],
            options={
                'db_table': 'cp',
                'verbose_name': 'cp',
                'verbose_name_plural': 'cp',
            },
        ),
        migrations.CreateModel(
            name='Media',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=32, verbose_name='\u540d\u79f0', db_index=True)),
            ],
            options={
                'db_table': 'media',
                'verbose_name': 'media',
                'verbose_name_plural': 'media',
            },
        ),
        migrations.CreateModel(
            name='Picture',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(default=b'', max_length=128, verbose_name='\u6807\u9898', db_index=True, blank=True)),
                ('desc', models.TextField(default=b'', verbose_name='\u63cf\u8ff0', blank=True)),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='\u5165\u5e93\u65f6\u95f4', db_index=True)),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='\u66f4\u65b0\u65f6\u95f4', db_index=True)),
                ('image_url', models.CharField(default=b'', max_length=1024, verbose_name='\u56fe\u7247\u5730\u5740')),
                ('category_set', models.ManyToManyField(related_name='album_category_set+', null=True, verbose_name='\u5206\u7c7b', to='picture.Category', blank=True)),
                ('cp', models.ForeignKey(related_name='+', verbose_name='CP', blank=True, to='picture.CP', null=True)),
                ('creator', models.ForeignKey(related_name='+', verbose_name='\u6700\u8fd1\u64cd\u4f5c\u8005', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('meida', models.ForeignKey(related_name='+', verbose_name='\u54c1\u724c', blank=True, to='picture.Media', null=True)),
            ],
            options={
                'db_table': 'picture',
                'verbose_name': '\u56fe\u7247',
                'verbose_name_plural': '\u56fe\u7247',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=32, verbose_name='\u540d\u79f0', db_index=True)),
            ],
            options={
                'db_table': 'tag',
                'verbose_name': '\u6807\u7b7e',
                'verbose_name_plural': '\u6807\u7b7e',
            },
        ),
        migrations.AddField(
            model_name='picture',
            name='tag_set',
            field=models.ManyToManyField(related_name='album_tag_set+', null=True, verbose_name='\u6807\u7b7e', to='picture.Tag', blank=True),
        ),
    ]
