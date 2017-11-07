# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('palabro', '0005_visit_visited_page'),
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('identifier', models.CharField(max_length=1)),
                ('description', models.CharField(max_length=50)),
                ('short_description', models.CharField(null=True, max_length=10, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('birthday', models.DateTimeField(null=True)),
                ('genre', models.ForeignKey(null=True, to='palabro.Genre')),
                ('native_language', models.ForeignKey(to='palabro.Language')),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='visitor',
            name='city',
            field=models.CharField(null=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='visitor',
            name='country_code',
            field=models.CharField(null=True, max_length=3),
        ),
        migrations.AlterField(
            model_name='visitor',
            name='country_code3',
            field=models.CharField(null=True, max_length=3),
        ),
        migrations.AlterField(
            model_name='visitor',
            name='latitude',
            field=models.CharField(null=True, max_length=25),
        ),
        migrations.AlterField(
            model_name='visitor',
            name='longitude',
            field=models.CharField(null=True, max_length=25),
        ),
    ]
