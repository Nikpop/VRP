# Generated by Django 3.0.4 on 2020-04-25 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0011_auto_20200425_1217'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='posy',
            field=models.FloatField(default=2),
        ),
        migrations.AlterField(
            model_name='posts',
            name='posz',
            field=models.FloatField(default=-3.8),
        ),
    ]
