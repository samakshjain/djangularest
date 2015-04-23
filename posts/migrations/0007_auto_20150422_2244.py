# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0006_auto_20150422_2244'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='upload_date',
            field=models.DateTimeField(auto_now_add=True),
            preserve_default=True,
        ),
    ]
