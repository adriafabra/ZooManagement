# Generated by Django 3.1.6 on 2021-04-07 16:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ZooWeb', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='worker',
            name='age',
        ),
        migrations.RemoveField(
            model_name='worker',
            name='surname',
        ),
    ]
