# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MyDiRa', '0003_answer_surveysetup'),
    ]

    operations = [
        migrations.RenameField(
            model_name='surveyresponses',
            old_name='interest023',
            new_name='interest03',
        ),
    ]
