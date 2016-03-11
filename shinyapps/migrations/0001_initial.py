# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ShinyGroup',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('username', models.CharField(max_length=50, default='')),
                ('selected', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='ShinyItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('itemid', models.CharField(max_length=20, default='')),
                ('name', models.CharField(max_length=50, default='')),
                ('dirname', models.CharField(max_length=50, default='')),
                ('group', models.ForeignKey(to='shinyapps.ShinyGroup', default=None)),
            ],
        ),
    ]
