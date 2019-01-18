# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import compte.models


class Migration(migrations.Migration):

    dependencies = [
        ('projets', '__first__'),
        ('ressources', '0002_compte_gl_employe'),
        ('compte', '0004_auto_20160203_1208'),
    ]

    operations = [
        migrations.CreateModel(
            name='Depense_Tpe',
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
                ('approved_by', models.ForeignKey(related_name='approving_employe_tpe', verbose_name='Approuv\xe9 par', blank=True, to='ressources.Employe', null=True)),
                ('employe', models.ForeignKey(verbose_name='Employ\xe9', to='ressources.Employe')),
                ('gl', models.ForeignKey(verbose_name='GL', to='ressources.Compte_gl')),
                ('projet', models.ForeignKey(verbose_name='Num\xe9ro de projet', to='projets.Projet_TPE')),
            ],
            options={
                'verbose_name': 'D\xe9pense Techno-Pro Expert',
                'verbose_name_plural': 'D\xe9penses Techno-Pro Expert',
                'permissions': (('creer_cdd_tpe', 'Creer une depense Techno-Pro Expert'), ('admin_cdd_tpe', 'Superviseur pour Techno-Pro Expert')),
            },
        ),
        migrations.CreateModel(
            name='Petite_Caisse_Eci',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateField(verbose_name='Date')),
                ('detail', models.CharField(max_length=50, verbose_name='D\xe9tails')),
                ('montant', models.DecimalField(default=0.0, verbose_name='Montant sans taxes', max_digits=12, decimal_places=2)),
                ('tps', models.DecimalField(default=0.0, verbose_name='TPS/TVH', max_digits=12, decimal_places=2)),
                ('tvq', models.DecimalField(default=0.0, verbose_name='TVQ', max_digits=12, decimal_places=2)),
                ('nb_penny', models.IntegerField(default=0, verbose_name='Nombre de 1 sous')),
                ('nb_nickel', models.IntegerField(default=0, verbose_name='Nombre de 5 sous')),
                ('nb_dime', models.IntegerField(default=0, verbose_name='Nombre de 10 sous')),
                ('nb_quarter', models.IntegerField(default=0, verbose_name='Nombre de 25 sous')),
                ('nb_cinq', models.IntegerField(default=0, verbose_name='Nombre de billet de 5')),
                ('nb_dix', models.IntegerField(default=0, verbose_name='Nombre de billet de 10')),
                ('nb_vingt', models.IntegerField(default=0, verbose_name='Nombre de billet de 20')),
                ('nb_cinquante', models.IntegerField(default=0, verbose_name='Nombre de billet de 50')),
                ('nb_cent', models.IntegerField(default=0, verbose_name='Nombre de billet de 100')),
                ('gl', models.ForeignKey(verbose_name='GL', to='ressources.Compte_gl')),
                ('projet', models.ForeignKey(verbose_name='Num\xe9ro de projet', to='projets.Projet_Eugenie')),
            ],
            options={
                'verbose_name': 'Petite caisse Eug\xe9nie Canada',
                'verbose_name_plural': 'Petite caisse Eug\xe9nie Canada',
                'permissions': (('creer_pc_eci', 'Creer depense petite caisse EuG\xe9nie'), ('admin_pc_eci', 'Superviseur pour EuG\xe9nie Canada Inc.')),
            },
        ),
        migrations.AlterModelOptions(
            name='depense_eci',
            options={'verbose_name': 'D\xe9pense Eug\xe9nie Canada', 'verbose_name_plural': 'D\xe9penses Eug\xe9nie Canada', 'permissions': (('creer_cdd_eci', 'Creer une depense EuG\xe9nie'), ('admin_cdd_eci', 'Superviseur pour EuG\xe9nie Canada Inc.'))},
        ),
    ]
