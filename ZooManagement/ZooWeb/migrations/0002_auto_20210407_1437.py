# Generated by Django 3.1.6 on 2021-04-07 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ZooWeb', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='GroupOfVisitors',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('representant', models.CharField(max_length=100)),
                ('number_of_visitors', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Sector',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('M', 'Mountain'), ('F', 'Freshwater'), ('W', 'Wetlands'), ('FO', 'Forest'), ('D', 'Desert'), ('S', 'Sea'), ('SA', 'Savannah'), ('J', 'Jungle')], max_length=2)),
            ],
        ),
        migrations.AlterField(
            model_name='animal',
            name='classes',
            field=models.CharField(choices=[('M', 'Mammal'), ('R', 'Reptile'), ('B', 'Bird'), ('A', 'Amphibian')], max_length=1),
        ),
    ]
