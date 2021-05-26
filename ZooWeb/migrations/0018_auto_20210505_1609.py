# Generated by Django 3.1.6 on 2021-05-05 16:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ZooWeb', '0017_auto_20210505_1021'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='groupofvisitor',
            name='representant',
        ),
        migrations.AddField(
            model_name='groupofvisitor',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]