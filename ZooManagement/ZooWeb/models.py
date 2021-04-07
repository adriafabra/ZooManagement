from django.db import models

# Create your models here.


class Animal(models.Model):
    TAXONOMY_LIST = (('M', 'Mammal'), ('R', 'Reptile'), ('B', 'Bird'), ('A', 'Amphibian'))
    ALIMENTATION_LIST = (('C', 'Carnivorous'), ('H', 'Herbivorous'), ('O', 'Omnivorous'),
                        ('F', 'Fruitarian'), ('I', 'Filter'), ('S', 'Scavenger'), 
                        ('I', 'Insectivorous'), ('P', 'Piscivorous'))
    SECTOR_LIST = (('M', 'Mountain'), ('F', 'Freshwater'), ('W', 'Wetlands'), ('FO', 'Forest'),
                ('D', 'Desert'), ('S', 'Sea'), ('SA', 'Savannah'), ('J', 'Jungle'))

    

    species = models.CharField(max_length=100)
    classes = models.CharField(max_length=100, choices=TAXONOMY_LIST)
    weight = models.IntegerField()
    height = models.IntegerField()
    life_expectancy = models.IntegerField()
    alimentation = models.CharField(max_length=100, choices=ALIMENTATION_LIST)
    sector = models.CharField(max_length=100, choices=SECTOR_LIST)
   

class Worker(models.Model):
    NSS = models.IntegerField()
    name = models.CharField(max_length=100)

class Sector(models.Model):
    SECTOR_LIST = (('M', 'Mountain'), ('F', 'Freshwater'), ('W', 'Wetlands'), ('FO', 'Forest'),
                ('D', 'Desert'), ('S', 'Sea'), ('SA', 'Savannah'), ('J', 'Jungle'))


    name = models.CharField(max_length=100, choices=SECTOR_LIST)

class GroupOfVisitors(models.Model):
    representant = models.CharField(max_length=100)
    number_of_visitors = models.IntegerField()

