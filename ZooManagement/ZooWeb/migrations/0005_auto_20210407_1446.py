# Generated by Django 3.1.6 on 2021-04-07 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ZooWeb', '0004_auto_20210407_1445'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animal',
            name='alimentation',
            field=models.CharField(choices=[('C', 'Carnivorous'), ('H', 'Herbivorous'), ('O', 'Omnivorous'), ('F', 'Fruitarian'), ('I', 'Filter'), ('S', 'Scavenger'), ('I', 'Insectivorous'), ('P', 'Piscivorous')], max_length=100),
        ),
        migrations.AlterField(
            model_name='animal',
            name='height',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='animal',
            name='life_expectancy',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='animal',
            name='sector',
            field=models.CharField(choices=[('M', 'Mountain'), ('F', 'Freshwater'), ('W', 'Wetlands'), ('FO', 'Forest'), ('D', 'Desert'), ('S', 'Sea'), ('SA', 'Savannah'), ('J', 'Jungle')], max_length=100),
        ),
        migrations.AlterField(
            model_name='animal',
            name='weight',
            field=models.IntegerField(),
        ),
    ]