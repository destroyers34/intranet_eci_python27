# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Compagnie',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nom', models.CharField(max_length=60, verbose_name='Nom')),
                ('code', models.CharField(max_length=3, null=True, verbose_name='Code', blank=True)),
            ],
            options={
                'verbose_name': 'Compagnie',
            },
        ),
        migrations.CreateModel(
            name='Compte_gl',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('numero', models.IntegerField(verbose_name='Num\xe9ro')),
                ('description', models.CharField(max_length=60, verbose_name='Description')),
                ('sens', models.CharField(default=b' ', max_length=2, verbose_name='Sens du solde', choices=[(b'DT', b'DT'), (b'CT', b'CT'), (b' ', b' ')])),
                ('type', models.CharField(default=b' ', max_length=1, verbose_name='Type de compte', choices=[(b'0', b'Poste'), (b'1', b'Rubrique'), (b'2', b'Total'), (b'3', b'Titre')])),
                ('solde', models.DecimalField(default=0.0, verbose_name='Solde', max_digits=12, decimal_places=3)),
                ('inactif', models.BooleanField(default=False, verbose_name='Inactif')),
            ],
        ),
        migrations.CreateModel(
            name='Devise',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nom', models.CharField(max_length=100, verbose_name='Nom')),
                ('code_iso', models.CharField(max_length=3, verbose_name='Code ISO')),
                ('symbole', models.CharField(max_length=3, verbose_name='Symbole')),
                ('taux_toCAD', models.DecimalField(default=b'1', verbose_name='Taux vers ($CA)', max_digits=13, decimal_places=10)),
                ('taux_inverse', models.DecimalField(default=b'1', verbose_name='Taux inverse', max_digits=13, decimal_places=10)),
                ('date_taux', models.DateField(verbose_name='Date des taux')),
            ],
        ),
        migrations.CreateModel(
            name='Employe',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('hire_date', models.DateField(null=True, verbose_name="Date d'embauche", blank=True)),
                ('banque_heure', models.DecimalField(default=0.0, verbose_name='Heure(s) en banque', max_digits=11, decimal_places=2)),
                ('taux_horaire', models.DecimalField(default=0.0, verbose_name='Taux horaire', max_digits=6, decimal_places=2)),
                ('compagnie', models.ForeignKey(verbose_name='Compagnie', blank=True, to='ressources.Compagnie', null=True)),
                ('superviseur', models.ForeignKey(blank=True, to='ressources.Employe', null=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['user__first_name'],
                'verbose_name': 'Employ\xe9',
            },
        ),
        migrations.CreateModel(
            name='Tache',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('numero', models.CharField(max_length=10, verbose_name='Num\xe9ro')),
                ('description', models.CharField(max_length=60, verbose_name='Description')),
                ('type', models.CharField(default=b'PO', max_length=2, verbose_name='Type de tache:', choices=[(b'PO', b'Positif'), (b'NE', b'N\xc3\xa9gatif')])),
            ],
            options={
                'ordering': ['numero'],
                'verbose_name': 'T\xe2che',
            },
        ),
        migrations.AddField(
            model_name='compte_gl',
            name='devise',
            field=models.ForeignKey(verbose_name='Devise', blank=True, to='ressources.Devise', null=True),
        ),
    ]
