# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-09-12 20:16
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_steps'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Steps',
            new_name='Step',
        ),
    ]