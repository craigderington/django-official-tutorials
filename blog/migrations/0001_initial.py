# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.utils.timezone import utc
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('created_date', models.DateTimeField(default=datetime.datetime(2015, 10, 15, 13, 46, 12, 505379, tzinfo=utc))),
                ('pub_date', models.DateTimeField(null=True, blank=True)),
                ('title', models.CharField(max_length=200)),
                ('blog_text', models.TextField()),
                ('slug', models.SlugField()),
                ('is_draft', models.BooleanField()),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
