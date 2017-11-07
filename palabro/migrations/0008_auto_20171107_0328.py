# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('palabro', '0007_auto_20171107_0234'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='birthday',
            new_name='birthdate',
        ),
    ]
