# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('MyDiRa', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SurveyResponses',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('career01', models.ForeignKey(to='MyDiRa.Careers')),
                ('career02', models.ForeignKey(related_name='c02', blank=True, to='MyDiRa.Careers', null=True)),
                ('demographic', models.ForeignKey(to='MyDiRa.Demographics')),
                ('gender', models.ForeignKey(to='MyDiRa.Genders')),
                ('interest01', models.ForeignKey(to='MyDiRa.Interests')),
                ('interest02', models.ForeignKey(related_name='i02', blank=True, to='MyDiRa.Interests', null=True)),
                ('interest023', models.ForeignKey(related_name='i03', blank=True, to='MyDiRa.Interests', null=True)),
                ('interest04', models.ForeignKey(related_name='i04', blank=True, to='MyDiRa.Interests', null=True)),
                ('interest05', models.ForeignKey(related_name='i05', blank=True, to='MyDiRa.Interests', null=True)),
                ('interest06', models.ForeignKey(related_name='i06', blank=True, to='MyDiRa.Interests', null=True)),
                ('interest07', models.ForeignKey(related_name='i07', blank=True, to='MyDiRa.Interests', null=True)),
                ('interest08', models.ForeignKey(related_name='i08', blank=True, to='MyDiRa.Interests', null=True)),
                ('interest09', models.ForeignKey(related_name='i09', blank=True, to='MyDiRa.Interests', null=True)),
                ('interest10', models.ForeignKey(related_name='i10', blank=True, to='MyDiRa.Interests', null=True)),
                ('orientation', models.ForeignKey(to='MyDiRa.Orientations')),
                ('relationship', models.ForeignKey(to='MyDiRa.Relationship')),
                ('year_of_birth', models.ForeignKey(to='MyDiRa.YearOfBirth')),
            ],
        ),
    ]
