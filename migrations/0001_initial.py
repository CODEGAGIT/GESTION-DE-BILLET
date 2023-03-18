# Generated by Django 3.1.2 on 2023-03-11 07:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='bus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('matricule_bus', models.CharField(max_length=12)),
                ('nb_place', models.PositiveSmallIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_clt', models.CharField(max_length=30)),
                ('prenom_clt', models.CharField(max_length=50)),
                ('email_clt', models.CharField(max_length=60)),
                ('telephone_clt', models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='compagnie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_cp', models.CharField(max_length=10)),
                ('siege_cp', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='date_depart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ladate', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='grade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('libelle_grd', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='heure_depart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('l_heure', models.TimeField(default='05:00.0')),
            ],
        ),
        migrations.CreateModel(
            name='reservation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nb_billet', models.PositiveSmallIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='suggestion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=20)),
                ('message', models.TextField(max_length=500)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='ville',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_ville', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='v_depart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ville_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='akst.ville')),
            ],
        ),
        migrations.CreateModel(
            name='v_arrivee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ville_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='akst.ville')),
            ],
        ),
        migrations.CreateModel(
            name='utilisateur',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_user', models.CharField(max_length=30)),
                ('prenom_user', models.CharField(max_length=50)),
                ('email_user', models.CharField(max_length=60)),
                ('id_user', models.CharField(max_length=10)),
                ('pw_user', models.CharField(max_length=12)),
                ('compagnie_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='akst.compagnie')),
                ('grade_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='akst.grade')),
            ],
        ),
        migrations.CreateModel(
            name='ligne',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prix', models.FloatField(default=0)),
                ('ville_arr', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='akst.v_arrivee')),
                ('ville_dep', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='akst.v_depart')),
            ],
        ),
        migrations.CreateModel(
            name='infoligne',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bus_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='akst.bus')),
                ('date_dep', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='akst.date_depart')),
                ('heure_dep', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='akst.heure_depart')),
                ('ligne_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='akst.ligne')),
            ],
        ),
        migrations.AddField(
            model_name='date_depart',
            name='infoln_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='akst.infoligne'),
        ),
        migrations.AddField(
            model_name='bus',
            name='compagnie_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='akst.compagnie'),
        ),
        migrations.CreateModel(
            name='billet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code_billet', models.PositiveIntegerField(default=0)),
                ('client_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='akst.client')),
                ('compagnie_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='akst.compagnie')),
                ('reservation_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='akst.reservation')),
            ],
        ),
    ]