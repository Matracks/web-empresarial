# Generated by Django 4.1 on 2022-08-17 19:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='published',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 17, 19, 8, 3, 246860, tzinfo=datetime.timezone.utc), verbose_name='Fecha de Publicación'),
        ),
    ]
