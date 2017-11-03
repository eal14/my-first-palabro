# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('palabro', '0002_visitor'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='visitor',
            name='id',
        ),
        migrations.AlterField(
            model_name='visitor',
            name='ip',
            field=models.CharField(max_length=128, serialize=False, primary_key=True),
        ),
    ]
