# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compte', '0006_petite_caisse_eci_employe'),
    ]

    operations = [
        migrations.AddField(
            model_name='petite_caisse_eci',
            name='nb_deux',
            field=models.IntegerField(default=0, verbose_name='Nombre de 2$'),
        ),
        migrations.AddField(
            model_name='petite_caisse_eci',
            name='nb_un',
            field=models.IntegerField(default=0, verbose_name='Nombre de 1$'),
        ),
    ]
