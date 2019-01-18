# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ressources', '0002_compte_gl_employe'),
        ('compte', '0002_auto_20160120_1726'),
    ]

    operations = [
        migrations.AddField(
            model_name='depense_eci',
            name='approved_by',
            field=models.ForeignKey(related_name='approving_employe', verbose_name='Approuv\xe9 par', blank=True, to='ressources.Employe', null=True),
        ),
        migrations.AddField(
            model_name='depense_eci',
            name='approved_on',
            field=models.DateTimeField(null=True, verbose_name='Approuv\xe9 le', blank=True),
        ),
    ]
