# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import compte.models


class Migration(migrations.Migration):

    dependencies = [
        ('projets', '__first__'),
        ('ressources', '0002_compte_gl_employe'),
    ]

    operations = [
        migrations.CreateModel(
            name='Depense_Eci',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateField(verbose_name='Date')),
                ('detail', models.CharField(max_length=50, verbose_name='D\xe9tails')),
                ('montant', models.DecimalField(default=0.0, verbose_name='Montant sans taxes', max_digits=12, decimal_places=2)),
                ('tps', models.DecimalField(default=0.0, verbose_name='TPS/TVH', max_digits=12, decimal_places=2)),
                ('tvq', models.DecimalField(default=0.0, verbose_name='TVQ', max_digits=12, decimal_places=2)),
                ('photo', models.ImageField(upload_to=compte.models.upload_path, blank=True)),
                ('approuve', models.BooleanField(default=False, verbose_name='Approuv\xe9?')),
                ('paye', models.BooleanField(default=False, verbose_name='Pay\xe9?')),
                ('approved_on', models.DateTimeField(null=True, verbose_name='Approuv\xe9 le', blank=True)),
                ('approved_by', models.ForeignKey(related_name='approving_employe', verbose_name='Approuv\xe9 par', to='ressources.Employe')),
                ('employe', models.ForeignKey(verbose_name='Employ\xe9', to='ressources.Employe')),
                ('gl', models.ForeignKey(verbose_name='GL', to='ressources.Compte_gl')),
                ('projet', models.ForeignKey(verbose_name='Num\xe9ro de projet', to='projets.Projet_Eugenie')),
            ],
            options={
                'verbose_name': 'D\xe9pense Eug\xe9nie Canada',
                'verbose_name_plural': 'D\xe9penses Eug\xe9nie Canada',
            },
        ),
    ]
