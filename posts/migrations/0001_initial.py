# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-10-03 10:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_ar', models.CharField(max_length=120)),
                ('title_fr', models.CharField(max_length=120)),
                ('category_ar', models.CharField(default='News', max_length=120)),
                ('category_fr', models.CharField(default='News', max_length=120)),
                ('image', models.ImageField(blank=True, height_field='height_field', null=True, upload_to=b'', width_field='width_field')),
                ('description_ar', models.TextField()),
                ('description_fr', models.TextField()),
                ('publish', models.DateField()),
                ('updated', models.DateTimeField(auto_now=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-timestamp', '-updated'],
            },
        ),
    ]