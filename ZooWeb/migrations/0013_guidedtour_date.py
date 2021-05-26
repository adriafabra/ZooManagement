# Generated by Django 3.1.6 on 2021-05-05 09:48

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('ZooWeb', '0012_remove_guidedtour_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='guidedtour',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]