# Generated by Django 3.1.2 on 2023-03-11 07:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('akst', '0002_remove_date_depart_infoln_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='date_depart',
            name='infoln_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='akst.infoligne'),
        ),
    ]
