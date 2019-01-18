# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Projet_Eugenie',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('numero', models.CharField(unique=True, max_length=30, verbose_name='Num\xe9ro du projet')),
                ('nom', models.CharField(default=b'X', max_length=30, verbose_name='Nom du projet')),
                ('date_soumission', models.DateField(null=True, verbose_name='Date de soumission', blank=True)),
                ('date_debut', models.DateField(default=django.utils.timezone.now, verbose_name='Date de d\xe9but')),
                ('date_fin', models.DateField(default=django.utils.timezone.now, verbose_name='Date de fin')),
                ('actif', models.BooleanField(verbose_name='Actif')),
                ('en_attente', models.BooleanField(verbose_name='En attente')),
                ('modele', models.CharField(default=b'X', max_length=30, verbose_name='Mod\xe8le')),
                ('serial_number', models.CharField(max_length=30, null=True, verbose_name='Num\xe9ro de s\xe9rie', blank=True)),
                ('budget_mat', models.DecimalField(default=0, verbose_name='Budget MAT ($)', max_digits=11, decimal_places=2)),
                ('budget_mo', models.DecimalField(default=0, verbose_name='Budget MO (H)', max_digits=11, decimal_places=2)),
                ('priority', models.DecimalField(default=b'9', verbose_name='Priorit\xe9', max_digits=2, decimal_places=0)),
                ('client', models.ForeignKey(verbose_name='Client', blank=True, to='clients.Compagnie', null=True)),
            ],
            options={
                'ordering': ['-numero'],
                'verbose_name': 'Projet EuG\xe9nie',
                'verbose_name_plural': 'Projets EuG\xe9nie',
            },
        ),
        migrations.CreateModel(
            name='Projet_TPE',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('numero', models.CharField(unique=True, max_length=30, verbose_name='Num\xe9ro du projet')),
                ('nom', models.CharField(default=b'X', max_length=30, verbose_name='Nom du projet')),
                ('date_soumission', models.DateField(null=True, verbose_name='Date de soumission', blank=True)),
                ('date_debut', models.DateField(default=django.utils.timezone.now, verbose_name='Date de d\xe9but')),
                ('date_fin', models.DateField(default=django.utils.timezone.now, verbose_name='Date de fin')),
                ('actif', models.BooleanField(verbose_name='Actif')),
                ('en_attente', models.BooleanField(verbose_name='En attente')),
                ('description', models.CharField(default=b'X', max_length=30, verbose_name='Description')),
                ('serial_number', models.CharField(max_length=30, null=True, verbose_name='Num\xe9ro de s\xe9rie', blank=True)),
                ('budget_mat', models.DecimalField(default=0, verbose_name='Budget MAT ($)', max_digits=11, decimal_places=2)),
                ('budget_mo', models.DecimalField(default=0, verbose_name='Budget MO (H)', max_digits=11, decimal_places=2)),
                ('client', models.ForeignKey(verbose_name='Client', blank=True, to='clients.Compagnie', null=True)),
            ],
            options={
                'ordering': ['-numero'],
                'verbose_name': 'Projet Techno-Pro Experts',
                'verbose_name_plural': 'Projets Techno-Pro Experts',
            },
        ),
    ]
