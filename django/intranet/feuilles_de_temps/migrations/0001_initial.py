# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projets', '0001_initial'),
        ('ressources', '0002_compte_gl_employe'),
    ]

    operations = [
        migrations.CreateModel(
            name='Banque',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateField(verbose_name='Date')),
                ('temps', models.DecimalField(verbose_name='Temps', max_digits=4, decimal_places=2)),
                ('employe', models.ForeignKey(verbose_name='Employ\xe9', to='ressources.Employe')),
            ],
            options={
                'verbose_name': 'Bloc Banque',
                'verbose_name_plural': 'Blocs Banque',
                'permissions': (('afficher_rapport_banque', 'Afficher un rapport de temps des heures en banque'),),
            },
        ),
        migrations.CreateModel(
            name='Bloc_Eugenie',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateField(verbose_name='Date')),
                ('temps', models.DecimalField(verbose_name='Temps', max_digits=4, decimal_places=2)),
                ('note', models.TextField(max_length=200, verbose_name='Commentaires', blank=True)),
                ('banque', models.BooleanField(default=False, verbose_name='Heures Banque')),
                ('approuve', models.BooleanField(default=False, verbose_name='Approuv\xe9')),
                ('employe', models.ForeignKey(verbose_name='Employ\xe9', to='ressources.Employe')),
                ('projet', models.ForeignKey(verbose_name='Projet', to='projets.Projet_Eugenie')),
                ('tache', models.ForeignKey(verbose_name='T\xe2che', to='ressources.Tache')),
            ],
            options={
                'verbose_name': 'Bloc Eug\xe9nie',
                'verbose_name_plural': 'Blocs Eug\xe9nie',
                'permissions': (('afficher_rapport_temps_eugenie', 'Afficher un rapport de temps EuG\xe9nie'), ('superviseur_eugenie', 'Superviseur pour EuG\xe9nie Canada Inc.')),
            },
        ),
        migrations.CreateModel(
            name='Bloc_TPE',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateField(verbose_name='Date')),
                ('temps', models.DecimalField(verbose_name='Temps', max_digits=4, decimal_places=2)),
                ('note', models.TextField(max_length=200, verbose_name='Commentaires', blank=True)),
                ('banque', models.BooleanField(default=False, verbose_name='Heures Banque')),
                ('approuve', models.BooleanField(default=False, verbose_name='Approuv\xe9')),
                ('employe', models.ForeignKey(verbose_name='Employ\xe9', to='ressources.Employe')),
                ('projet', models.ForeignKey(verbose_name='Projet', to='projets.Projet_TPE')),
                ('tache', models.ForeignKey(verbose_name='T\xe2che', to='ressources.Tache')),
            ],
            options={
                'verbose_name': 'Bloc Techno-Pro Experts',
                'verbose_name_plural': 'Blocs Techno-Pro Experts',
                'permissions': (('afficher_rapport_temps_tpe', 'Afficher un rapport de temps TPE'),),
            },
        ),
    ]
