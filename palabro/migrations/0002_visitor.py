# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('palabro', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Visitor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('ip', models.CharField(max_length=128)),
                ('created_dtim', models.DateTimeField(default=django.utils.timezone.now)),
                ('city', models.CharField(max_length=100)),
                ('country_code', models.CharField(max_length=3)),
                ('country_code3', models.CharField(max_length=3)),
                ('latitude', models.CharField(max_length=25)),
                ('longitude', models.CharField(max_length=25)),
                ('counter', models.IntegerField()),
            ],
        ),
    ]
