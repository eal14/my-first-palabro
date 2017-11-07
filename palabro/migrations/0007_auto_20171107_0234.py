# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('palabro', '0006_auto_20171107_0214'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='native_language',
            field=models.ForeignKey(to='palabro.Language', null=True),
        ),
    ]
