# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-03-04 19:06
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('referrals', '0003_auto_20181121_1129'),
    ]

    operations = [
        migrations.AlterField(
            model_name='referral',
            name='target_content_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='contenttypes.ContentType'),
        ),
        migrations.AlterField(
            model_name='referral',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='referral_codes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='referralresponse',
            name='ip_address',
            field=models.CharField(max_length=265),
        ),
        migrations.AlterField(
            model_name='referralresponse',
            name='target_content_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='contenttypes.ContentType'),
        ),
    ]
