# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booktest', '0005_auto_20210908_1315'),
    ]

    operations = [
        migrations.CreateModel(
            name='AreaInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('atitle', models.CharField(max_length=20)),
                ('aParent', models.ForeignKey(blank=True, null=True, to='booktest.AreaInfo')),
            ],
        ),
        migrations.AlterField(
            model_name='heroinfo',
            name='hcomment',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
