# Generated by Django 2.0.1 on 2018-03-30 05:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20180330_0855'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='end_time',
            field=models.DateTimeField(null=True),
        ),
    ]
