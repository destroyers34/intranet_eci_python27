# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projets', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categorie',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nom', models.CharField(unique=True, max_length=60, verbose_name='Cat\xe9gorie')),
            ],
            options={
                'ordering': ['nom'],
                'verbose_name': 'Cat\xe9gorie',
            },
        ),
        migrations.CreateModel(
            name='Fournisseur',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nom', models.CharField(unique=True, max_length=100, verbose_name='Nom')),
            ],
            options={
                'ordering': ['nom'],
                'verbose_name': 'Fournisseur',
            },
        ),
        migrations.CreateModel(
            name='Materiel_Eugenie',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateField(verbose_name='Date')),
                ('montant', models.DecimalField(verbose_name='Montant', max_digits=12, decimal_places=2)),
                ('categorie', models.ForeignKey(verbose_name='Cat\xe9gorie', to='budget_materiel.Categorie')),
                ('fournisseur', models.ForeignKey(verbose_name='Fournisseur', to='budget_materiel.Fournisseur', null=True)),
                ('projet', models.ForeignKey(verbose_name='Projet', to='projets.Projet_Eugenie')),
            ],
            options={
                'verbose_name': 'Mat\xe9riel Eug\xe9nie',
                'verbose_name_plural': 'Mat\xe9riel Eug\xe9nie',
            },
        ),
    ]
