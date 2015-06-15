# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('joins', '0002_auto_20150614_1644'),
    ]

    operations = [
        migrations.AddField(
            model_name='join',
            name='join_reason',
            field=models.CharField(default=b'MW', max_length=2, choices=[(b'MW', b'Martian_War'), (b'IT', b'Interstellar Travel'), (b'FJ', b'Fleeing Justice'), (b'MC', b'Meet Chicks')]),
        ),
    ]
