# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('pub_date', models.DateField(default=datetime.datetime(2015, 4, 21, 4, 33, 5, 783535, tzinfo=utc), verbose_name=b'date published')),
                ('is_featured', models.BooleanField(default=False)),
                ('headline', models.CharField(default=b'No headline yet', max_length=100)),
                ('article_body', models.TextField(default=b'No article body yet')),
                ('url', models.CharField(default=b'No link yet', max_length=512)),
            ],
        ),
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default=b'No author yet', max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default=b'No section yet', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('iphone_udid', models.CharField(max_length=256)),
                ('favorite_articles', models.ManyToManyField(to='tsl_news.Article')),
            ],
        ),
        migrations.CreateModel(
            name='WaitingArticle',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('url', models.CharField(max_length=512)),
            ],
        ),
        migrations.AddField(
            model_name='article',
            name='authors',
            field=models.ManyToManyField(to='tsl_news.Author'),
        ),
        migrations.AddField(
            model_name='article',
            name='section',
            field=models.ForeignKey(to='tsl_news.Section', null=True),
        ),
    ]
