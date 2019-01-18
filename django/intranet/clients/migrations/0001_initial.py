# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Compagnie',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nom', models.CharField(max_length=50, default='Entrez un nom', verbose_name='Nom')),
                ('adresse', models.CharField(max_length=50, verbose_name='Adresse', blank=True)),
                ('ville', models.CharField(max_length=50, verbose_name='Ville', blank=True)),
                ('province_etat', models.CharField(max_length=50, verbose_name='Province/\xc9tat', blank=True)),
                ('postal_code', models.CharField(max_length=50, verbose_name='Code Postal', blank=True)),
                ('pays', models.CharField(max_length=50, verbose_name='Pays', blank=True)),
                ('telephonne', models.CharField(max_length=50, verbose_name='Num\xe9ro de t\xe9l\xe9phonne', blank=True)),
                ('fax', models.CharField(max_length=50, verbose_name='Num\xe9ro de fax', blank=True)),
            ],
            options={
                'verbose_name': 'Compagnie',
            },
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('prenom', models.CharField(max_length=50, verbose_name='Pr\xe9nom', blank=True)),
                ('nom', models.CharField(max_length=50, verbose_name='Nom', blank=True)),
                ('fonction', models.CharField(max_length=50, verbose_name='Fonction', blank=True)),
                ('telephonne', models.CharField(max_length=50, verbose_name='Num\xe9ro de t\xe9l\xe9phonne', blank=True)),
                ('email', models.CharField(max_length=50, verbose_name='Adresse courriel', blank=True)),
                ('compagnie', models.ForeignKey(verbose_name='Compagnie', to='clients.Compagnie')),
            ],
            options={
                'ordering': ['prenom', 'nom'],
                'verbose_name': 'Contact',
            },
        ),
    ]
