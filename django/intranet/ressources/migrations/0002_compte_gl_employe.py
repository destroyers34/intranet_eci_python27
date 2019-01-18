# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ressources', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='compte_gl',
            name='employe',
            field=models.ForeignKey(blank=True, to='ressources.Employe', null=True),
        ),
    ]
