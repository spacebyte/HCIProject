# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-22 21:15
from __future__ import unicode_literals

from django.db import migrations, models
import django_mysql.models


class Migration(migrations.Migration):

    dependencies = [
        ('hciproject', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answers', django_mysql.models.JSONField(default=dict)),
                ('question', models.CharField(max_length=264)),
                ('image', models.ImageField(blank=True, upload_to=b'question_images')),
                ('category', models.CharField(choices=[(b'L', b'Location'), (b'T', b'Trivia'), (b'H', b'History'), (b'P', b'People')], default=b'T', max_length=1)),
            ],
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='website',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='location',
            field=models.CharField(choices=[(b'C', b'City Centre'), (b'K', b'Kelvindale'), (b'P', b'Partick')], default=b'C', max_length=1),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='score',
            field=django_mysql.models.JSONField(default=dict),
        ),
    ]