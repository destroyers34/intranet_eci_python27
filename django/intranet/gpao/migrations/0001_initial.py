# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Famille',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('reference', models.CharField(unique=True, max_length=30, verbose_name='# R\xe9f\xe9rence:')),
                ('designation', models.CharField(max_length=100, verbose_name='D\xe9signation:')),
            ],
            options={
                'ordering': ['reference'],
                'verbose_name': 'Famille',
                'verbose_name_plural': 'Familles',
            },
        ),
        migrations.CreateModel(
            name='Fournisseur',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nom', models.CharField(max_length=100, verbose_name='Nom:')),
            ],
        ),
        migrations.CreateModel(
            name='LienNM',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('numero_pe', models.IntegerField(verbose_name='# sur le PE:')),
                ('quantite', models.IntegerField(verbose_name='Quantit\xe9:')),
            ],
        ),
        migrations.CreateModel(
            name='LienPiece',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('numero_pe', models.IntegerField(verbose_name='# sur le PE:')),
                ('quantite', models.IntegerField(verbose_name='Quantit\xe9:')),
            ],
        ),
        migrations.CreateModel(
            name='Nm',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('reference', models.CharField(unique=True, max_length=30, verbose_name='# R\xe9f\xe9rence:')),
                ('designation', models.CharField(max_length=100, verbose_name='D\xe9signation:')),
                ('categorie', models.CharField(default=b'AS', max_length=2, verbose_name='Cat\xe9gorie de NM:', choices=[(b'AS', b'Assy System'), (b'WP', b'Wiring Pneumatic'), (b'WE', b'Wiring Electric'), (b'MA', b'Machine'), (b'SO', b'Software'), (b'RF', b'R\xc3\xa9trofit'), (b'MO', b'Modernisation'), (b'RE', b'R\xc3\xa9paration'), (b'SC', b'Setup Clamp')])),
                ('liens', models.ManyToManyField(related_name='related_to', verbose_name='Contient les NMs suivant:', through='gpao.LienNM', to='gpao.Nm')),
            ],
            options={
                'ordering': ['reference'],
                'verbose_name': 'Nomenclature',
                'verbose_name_plural': 'Nomenclatures',
            },
        ),
        migrations.CreateModel(
            name='Pe',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('reference', models.CharField(unique=True, max_length=30, verbose_name='# R\xe9f\xe9rence:')),
                ('plan', models.FileField(upload_to=b"PLANS D'ENSEMBLE (PE-XXXX)")),
            ],
            options={
                'ordering': ['reference'],
                'verbose_name': "Plan d'ensemble",
                'verbose_name_plural': "Plan d'ensembles",
            },
        ),
        migrations.CreateModel(
            name='Piece',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('reference', models.CharField(unique=True, max_length=30, verbose_name='# R\xe9f\xe9rence:')),
                ('plan', models.FileField(null=True, upload_to=b'PLANS DE DEFINITION (X__-XXXX)', blank=True)),
                ('designation', models.CharField(max_length=100, verbose_name='D\xe9signation:')),
                ('date', models.DateField(default=datetime.date.today, verbose_name='Date:')),
                ('format_papier', models.CharField(default=b'LT', max_length=2, verbose_name='Format papier:', choices=[(b'LT', b'Letter'), (b'LD', b'Ledger'), (b'A4', b'A4'), (b'OT', b'Autre')])),
                ('ref_commercial', models.CharField(default=b'XXX', max_length=30, verbose_name='R\xe9f\xe9rence commercial:')),
                ('ref_mecanique', models.CharField(default=b'XXX', max_length=30, verbose_name='R\xe9f\xe9rence m\xe9canique:')),
                ('brute', models.CharField(default=b'XXX', max_length=30, verbose_name='Brute:')),
                ('soudure', models.BooleanField(default=False, verbose_name='Soudure:')),
                ('finition', models.CharField(default=b'XX', max_length=2, verbose_name='Finition:', choices=[(b'XX', b'Aucune'), (b'ZP', b'Zinc Plated'), (b'AN', b'Anodisation'), (b'PE', b'Peint'), (b'PL', b'Placage'), (b'OB', b'Oxide Noir'), (b'BR', b'Bross\xc3\xa9'), (b'OT', b'Autre')])),
                ('commentaires', models.CharField(max_length=200, null=True, verbose_name='Commentaires:', blank=True)),
                ('prix', models.DecimalField(default=0.0, verbose_name='Prix:', max_digits=6, decimal_places=2)),
                ('famille', models.ForeignKey(verbose_name='Famille:', to='gpao.Famille')),
                ('fournisseur', models.ForeignKey(verbose_name='Fournisseur:', blank=True, to='gpao.Fournisseur', null=True)),
            ],
            options={
                'ordering': ['reference'],
                'verbose_name': 'Pi\xe8ce',
                'verbose_name_plural': 'Pi\xe8ces',
            },
        ),
        migrations.AddField(
            model_name='nm',
            name='liens_piece',
            field=models.ManyToManyField(related_name='related_piece', verbose_name='Contient les Pi\xe8ces suivante:', through='gpao.LienPiece', to='gpao.Piece'),
        ),
        migrations.AddField(
            model_name='nm',
            name='pe',
            field=models.ForeignKey(verbose_name="Plan d'ensemble:", blank=True, to='gpao.Pe', null=True),
        ),
        migrations.AddField(
            model_name='lienpiece',
            name='from_nm',
            field=models.ForeignKey(related_name='from_nm_p', to='gpao.Nm'),
        ),
        migrations.AddField(
            model_name='lienpiece',
            name='to_piece',
            field=models.ForeignKey(related_name='to_piece', verbose_name='Li\xe9 \xe0 Pi\xe8ce:', to='gpao.Piece'),
        ),
        migrations.AddField(
            model_name='liennm',
            name='from_nm',
            field=models.ForeignKey(related_name='from_nm', to='gpao.Nm'),
        ),
        migrations.AddField(
            model_name='liennm',
            name='to_nm',
            field=models.ForeignKey(related_name='to_nm', verbose_name='Li\xe9 \xe0 NM:', to='gpao.Nm'),
        ),
    ]
