# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ressources', '0002_compte_gl_employe'),
        ('compte', '0005_auto_20160223_1420'),
    ]

    operations = [
        migrations.AddField(
            model_name='petite_caisse_eci',
            name='employe',
            field=models.ForeignKey(default=1, verbose_name='Employ\xe9', to='ressources.Employe'),
            preserve_default=False,
        ),
    ]
