# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_post_pic'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='pic',
        ),
    ]
