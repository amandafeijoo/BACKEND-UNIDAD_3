# Generated by Django 5.0.6 on 2024-05-20 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='artist',
            name='genre',
            field=models.CharField(default='unknown', max_length=200),
        ),
    ]
