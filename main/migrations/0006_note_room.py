# Generated by Django 2.0.1 on 2018-03-31 01:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20180331_0718'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='room',
            field=models.IntegerField(default=0),
        ),
    ]
