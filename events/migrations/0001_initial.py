# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-26 21:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128, unique=True)),
                ('logo', models.FileField(blank=True, null=True, upload_to=b'')),
                ('image', models.FileField(blank=True, null=True, upload_to=b'')),
                ('body', models.TextField()),
                ('created_at', models.DateField(auto_now_add=True, db_index=True)),
                ('updated_at', models.DateField()),
            ],
        ),
    ]
