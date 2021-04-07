from django.db import models

# Create your models here.


class Animal(models.Model):

    TAXONOMY_LIST = (('M', 'Mammal'), ('R', 'Reptile'), ('B', 'Bird'), ('A', 'Amphibian'))
    ALIMENTATION_LIST = (('C', 'Carnivorous'), ('H', 'Herbivorous'), ('O', 'Omnivorous'),
                        ('F', 'Fruitarian'), ('I', 'Filter'), ('S', 'Scavenger'), 
                        ('I', 'Insectivorous'), ('P', 'Piscivorous'))

    

    species = models.CharField(max_length=20)
    classes = models.CharField(max_length=1, choices=TAXONOMY_LIST)
    weight = models.IntegerField()
    height = models.IntegerField()
    life_expectancy = models.IntegerField()
    alimentation = models.CharField(max_length=2, choices=ALIMENTATION_LIST)
    sector = models.ForeignKey('Sector', on_delete=models.CASCADE)
   

class Worker(models.Model):

    NSS = models.IntegerField()
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
    age = models.IntegerField()

class Sector(models.Model):
    SECTOR_LIST = (('M', 'Mountain'), ('F', 'Freshwater'), ('W', 'Wetlands'), ('FO', 'Forest'),
                ('D', 'Desert'), ('S', 'Sea'), ('SA', 'Savannah'), ('J', 'Jungle'))


    name = models.CharField(max_length=2, choices=SECTOR_LIST)

class GroupOfVisitor(models.Model):
    representant = models.CharField(max_length=20)
    number_of_visitors = models.IntegerField()

