# Generated by Django 2.2.6 on 2019-10-17 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_posts_background'),
    ]

    operations = [
        migrations.AddField(
            model_name='posts',
            name='terrain',
            field=models.CharField(default='City', max_length=255),
        ),
    ]
