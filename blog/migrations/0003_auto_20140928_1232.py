# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20140928_1220'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='entry',
            options={'ordering': ['-created'], 'verbose_name': 'Blog Entry', 'verbose_name_plural': 'Blog Entries'},
        ),
        migrations.RemoveField(
            model_name='entry',
            name='posted',
        ),
        migrations.AddField(
            model_name='entry',
            name='created',
            field=models.DateTimeField(default=datetime.date(2014, 9, 28), auto_now_add=True, db_index=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='entry',
            name='modified',
            field=models.DateTimeField(default=datetime.date(2014, 9, 28), auto_now=True),
            preserve_default=False,
        ),
    ]
