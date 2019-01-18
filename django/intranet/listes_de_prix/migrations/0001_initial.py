# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ressources', '0002_compte_gl_employe'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categorie',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nom', models.CharField(unique=True, max_length=30, verbose_name='Nom')),
                ('nom_en', models.CharField(unique=True, max_length=30, verbose_name='Nom Anglais')),
            ],
            options={
                'ordering': ['nom', 'nom_en'],
            },
        ),
        migrations.CreateModel(
            name='Fournisseur',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nom', models.CharField(max_length=100, verbose_name='Nom')),
                ('telephonne', models.CharField(max_length=100, null=True, verbose_name='Num\xe9ro de t\xe9l\xe9phonne', blank=True)),
                ('fax', models.CharField(max_length=100, null=True, verbose_name='Num\xe9ro de fax', blank=True)),
                ('siteweb', models.CharField(max_length=100, null=True, verbose_name='Site web', blank=True)),
                ('ratio', models.DecimalField(default=b'1', verbose_name='Ratio', max_digits=5, decimal_places=2)),
                ('ratio_us', models.DecimalField(default=b'1', verbose_name='Ratio US', max_digits=5, decimal_places=2)),
                ('actif', models.BooleanField(verbose_name='Actif')),
                ('devise', models.ForeignKey(verbose_name='Devise', to='ressources.Devise')),
            ],
            options={
                'ordering': ['nom'],
            },
        ),
        migrations.CreateModel(
            name='Machine',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('numero', models.CharField(unique=True, max_length=100, verbose_name='Num\xe9ro')),
                ('details', models.TextField(null=True, verbose_name='D\xe9tails', blank=True)),
                ('details_en', models.TextField(null=True, verbose_name='D\xe9tails Anglais', blank=True)),
                ('prix_fournisseur', models.DecimalField(verbose_name='Prix du fournisseur', max_digits=9, decimal_places=2)),
                ('dateprix', models.DateField(null=True, verbose_name='Date du prix', blank=True)),
                ('escompte', models.DecimalField(default=b'0', verbose_name='Escompte (%)', max_digits=5, decimal_places=2)),
                ('ratio', models.DecimalField(default=b'0', verbose_name='Ratio', max_digits=5, decimal_places=2)),
                ('ratio_us', models.DecimalField(default=b'0', verbose_name='Ratio US', max_digits=5, decimal_places=2)),
                ('description', models.CharField(max_length=50, null=True, verbose_name='Nom', blank=True)),
                ('actif', models.BooleanField(verbose_name='Actif')),
                ('categorie', models.ForeignKey(verbose_name='Cat\xe9gorie', to='listes_de_prix.Categorie')),
                ('fournisseur', models.ForeignKey(verbose_name='Fournisseur', to='listes_de_prix.Fournisseur')),
            ],
            options={
                'ordering': ['numero'],
                'abstract': False,
                'permissions': (('afficher_listes_prix', 'Afficher les listes de prix'), ('afficher_listes_prix_en', 'Afficher les listes de prix US')),
            },
        ),
        migrations.CreateModel(
            name='Option',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('numero', models.CharField(unique=True, max_length=100, verbose_name='Num\xe9ro')),
                ('details', models.TextField(null=True, verbose_name='D\xe9tails', blank=True)),
                ('details_en', models.TextField(null=True, verbose_name='D\xe9tails Anglais', blank=True)),
                ('prix_fournisseur', models.DecimalField(verbose_name='Prix du fournisseur', max_digits=9, decimal_places=2)),
                ('dateprix', models.DateField(null=True, verbose_name='Date du prix', blank=True)),
                ('escompte', models.DecimalField(default=b'0', verbose_name='Escompte (%)', max_digits=5, decimal_places=2)),
                ('ratio', models.DecimalField(default=b'0', verbose_name='Ratio', max_digits=5, decimal_places=2)),
                ('ratio_us', models.DecimalField(default=b'0', verbose_name='Ratio US', max_digits=5, decimal_places=2)),
                ('fournisseur', models.ForeignKey(verbose_name='Fournisseur', to='listes_de_prix.Fournisseur')),
                ('machines', models.ManyToManyField(related_name='options_machine', to='listes_de_prix.Machine')),
            ],
            options={
                'ordering': ['numero'],
                'abstract': False,
                'permissions': (('afficher_listes_prix', 'Afficher les listes de prix'), ('afficher_listes_prix_en', 'Afficher les listes de prix US')),
            },
        ),
    ]
