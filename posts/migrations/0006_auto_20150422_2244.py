# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_remove_post_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='upload_date',
            field=models.DateTimeField(auto_now=True),
            preserve_default=True,
        ),
    ]
