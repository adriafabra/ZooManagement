# Generated by Django 3.1.6 on 2021-05-05 09:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ZooWeb', '0013_guidedtour_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='guidedtour',
            name='date',
        ),
    ]