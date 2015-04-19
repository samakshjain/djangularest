# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='tagline',
            field=models.CharField(default='hi', max_length=140, blank=True),
            preserve_default=False,
        ),
    ]
