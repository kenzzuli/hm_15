# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booktest', '0002_auto_20210908_1311'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookinfo',
            name='bprice',
            field=models.DecimalField(default=9.88, max_digits=10, decimal_places=2),
        ),
    ]
