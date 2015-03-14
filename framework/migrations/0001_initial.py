# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import cloudinary.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('choice_text', models.CharField(max_length=200)),
                ('votes', models.IntegerField(default=0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Music',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('product_type', models.CharField(max_length=1, choices=[(b'S', b'Song'), (b'A', b'Album'), (b'C', b'Collection')])),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name=b'Date product created')),
                ('product_picture', cloudinary.models.CloudinaryField(max_length=100, null=True, verbose_name=b'image', blank=True)),
                ('average_score', models.PositiveSmallIntegerField(null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Musician',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('birth_date', models.DateField()),
                ('artist_name', models.CharField(max_length=50, blank=True)),
                ('description', models.TextField(blank=True)),
                ('website', models.URLField(blank=True)),
                ('email', models.EmailField(max_length=75)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name=b'Date account created')),
                ('profile_picture', cloudinary.models.CloudinaryField(max_length=100, null=True, verbose_name=b'image', blank=True)),
                ('number_reviews_received', models.PositiveSmallIntegerField(null=True, blank=True)),
                ('number_products', models.PositiveSmallIntegerField(null=True, blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Poll',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('question', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(verbose_name=b'date published')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100)),
                ('body', models.TextField(blank=True)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name=b'Date review created')),
                ('score', models.PositiveSmallIntegerField()),
                ('musician', models.ForeignKey(to='framework.Musician')),
                ('product', models.ForeignKey(to='framework.Music')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Reviewer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('birth_date', models.DateField()),
                ('artist_name', models.CharField(max_length=50, blank=True)),
                ('description', models.TextField(blank=True)),
                ('website', models.URLField(blank=True)),
                ('email', models.EmailField(max_length=75)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name=b'Date account created')),
                ('profile_picture', cloudinary.models.CloudinaryField(max_length=100, null=True, verbose_name=b'image', blank=True)),
                ('number_reviews_performed', models.PositiveSmallIntegerField(null=True, blank=True)),
                ('job_title', models.CharField(max_length=50, blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='review',
            name='reviewer',
            field=models.ForeignKey(to='framework.Reviewer'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='music',
            name='musician',
            field=models.ForeignKey(to='framework.Musician'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='choice',
            name='poll',
            field=models.ForeignKey(to='framework.Poll'),
            preserve_default=True,
        ),
    ]
