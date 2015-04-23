# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import posts.models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0007_auto_20150422_2244'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='pic',
            field=models.ImageField(null=True, upload_to=posts.models.get_image_path, blank=True),
            preserve_default=True,
        ),
    ]
