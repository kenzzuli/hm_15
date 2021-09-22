# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booktest', '0003_auto_20210908_1313'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bookinfo',
            name='bprice',
        ),
    ]
