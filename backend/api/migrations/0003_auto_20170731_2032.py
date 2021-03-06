# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-31 20:32
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20170730_2143'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='country',
            options={'ordering': ('code',)},
        ),
        migrations.RenameField(
            model_name='user',
            old_name='country',
            new_name='countries',
        ),
        migrations.AlterField(
            model_name='pinned',
            name='country',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Country'),
        ),
        migrations.AlterField(
            model_name='pinned',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
