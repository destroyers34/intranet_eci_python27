# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compte', '0003_auto_20160120_1734'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='depense_eci',
            options={'verbose_name': 'D\xe9pense Eug\xe9nie Canada', 'verbose_name_plural': 'D\xe9penses Eug\xe9nie Canada', 'permissions': (('creer_cdd_eci', 'Afficher un rapport de temps EuG\xe9nie'), ('admin_cdd_eci', 'Superviseur pour EuG\xe9nie Canada Inc.'))},
        ),
    ]
