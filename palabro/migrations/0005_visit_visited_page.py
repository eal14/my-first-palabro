# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('palabro', '0004_visit'),
    ]

    operations = [
        migrations.AddField(
            model_name='visit',
            name='visited_page',
            field=models.CharField(max_length=40, default=''),
            preserve_default=False,
        ),
    ]
