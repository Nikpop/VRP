# Generated by Django 3.0.4 on 2020-04-25 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0010_auto_20200425_1103'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='posx',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='posts',
            name='posy',
            field=models.FloatField(default=3.8),
        ),
        migrations.AlterField(
            model_name='posts',
            name='posz',
            field=models.FloatField(default=3.8),
        ),
    ]
