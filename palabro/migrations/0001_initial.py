# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('description', models.CharField(max_length=50)),
                ('short_description', models.CharField(null=True, blank=True, max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Phrase',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('description', models.CharField(max_length=1000)),
                ('abreviation', models.CharField(null=True, blank=True, max_length=20)),
                ('language', models.ForeignKey(to='palabro.Language')),
            ],
        ),
        migrations.CreateModel(
            name='RelationType',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('description', models.CharField(max_length=50)),
                ('short_description', models.CharField(null=True, blank=True, max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Thing',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('description', models.CharField(max_length=100)),
                ('abreviation', models.CharField(null=True, blank=True, max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='WordType',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('description', models.CharField(max_length=50)),
                ('short_description', models.CharField(null=True, blank=True, max_length=10)),
            ],
        ),
    ]
