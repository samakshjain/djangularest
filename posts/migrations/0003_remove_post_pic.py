# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20150422_1903'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='pic',
        ),
    ]
