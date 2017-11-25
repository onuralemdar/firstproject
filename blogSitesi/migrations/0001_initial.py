# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-25 13:14
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Gonderi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('baslik', models.CharField(max_length=200)),
                ('icerik', models.TextField()),
                ('y_tarihi', models.DateTimeField(blank=True, null=True)),
                ('tag', models.CharField(blank=True, max_length=300, null=True)),
                ('yazar', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
