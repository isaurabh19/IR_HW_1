# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-30 12:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donationApp', '0003_donationmodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='donationmodel',
            name='donor_contact',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='donationmodel',
            name='donor_email',
            field=models.EmailField(default='sample@sample.com', max_length=254),
        ),
        migrations.AddField(
            model_name='donationmodel',
            name='receiver_email',
            field=models.EmailField(default='sample@sample.com', max_length=254),
        ),
        migrations.AlterField(
            model_name='donationmodel',
            name='donor',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='donationmodel',
            name='receiver',
            field=models.CharField(max_length=100),
        ),
    ]
