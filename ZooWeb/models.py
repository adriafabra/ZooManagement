from django.db import models
from django.urls.base import reverse
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator,  MaxValueValidator

# Create your models here.


class Animal(models.Model):
    TAXONOMY_LIST = (('Mammal', 'Mammal'), ('Reptile', 'Reptile'), ('Bird', 'Bird'), ('Amphibian', 'Amphibian'))
    ALIMENTATION_LIST = (('Carnivorous', 'Carnivorous'), ('Herbivorous', 'Herbivorous'), ('Omnivorous', 'Omnivorous'),
                        ('Fruitarian', 'Fruitarian'), ('Filter', 'Filter'), ('Scavenger', 'Scavenger'), 
                        ('Insectivorous', 'Insectivorous'), ('Piscivorous', 'Piscivorous'))

    species = models.CharField(max_length=20, unique=True)
    classes = models.CharField(max_length=20, choices=TAXONOMY_LIST)
    weight_in_kilograms = models.IntegerField()
    height_in_centimeters = models.IntegerField()
    life_expectancy = models.IntegerField()
    alimentation = models.CharField(max_length=20, choices=ALIMENTATION_LIST)
    sector = models.ForeignKey('Sector', on_delete=models.CASCADE)

    def __str__(self):
        return self.species
   

class Worker(models.Model):
    NSS = models.IntegerField(unique=True)
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
    age = models.IntegerField()
    animals = models.ManyToManyField('Animal', blank=True)
    sectors = models.ManyToManyField('Sector', blank=True)

    def __str__(self):
        return "%s %s" % (self.name, self.surname)
    

class Sector(models.Model):
    SECTOR_LIST = (('Mountain', 'Mountain'), ('Freshwater', 'Freshwater'), ('Wetlands', 'Wetlands'), ('Forest', 'Forest'),
                ('Desert', 'Desert'), ('Sea', 'Sea'), ('Savannah', 'Savannah'), ('Jungle', 'Jungle'))

    name = models.CharField(max_length=20, choices=SECTOR_LIST, unique=True)
    area_in_square_meters = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    

class GroupOfVisitor(models.Model):
    HOUR_LIST = (('10:00', '10:00'), ('13:00', '13:00'), ('16:00', '16:00'), ('19:00', '19:00'))
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    number_of_visitors = models.IntegerField()
    sector = models.ManyToManyField('Sector')
    date = models.DateField()
    hour = models.CharField(max_length=20, choices=HOUR_LIST)
    user_city = models.CharField(max_length=120)
    user_region = models.CharField(max_length=120)
    user_country = models.CharField(max_length=120)
    user_phone = models.IntegerField(validators=[MinValueValidator(600000000),MaxValueValidator(799999999)])

    class Meta:
        unique_together = ('date', 'hour')

    def __str__(self):
        return "%s - %s %s" % (self.user.username, self.date, self.hour)

    def get_absolute_url(self):
        return reverse('visitors_detail', kwargs={'pk': self.pk})

class GuidedTour(models.Model):
    worker = models.ForeignKey('Worker', on_delete=models.CASCADE)
    group_of_visitor = models.ForeignKey('GroupOfVisitor', on_delete=models.CASCADE)
    
    def __str__(self):
        return "%s - %s %s" % (self.group_of_visitor.user, self.worker.name, self.worker.surname)

