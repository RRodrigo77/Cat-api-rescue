'''Models para cats.'''

from django.db import models

class Cats(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    breed_type = models.CharField(max_length=100)
    age = models.IntegerField()
    gender_choices = [
        ('M', 'Masculino'),
        ('F', 'Feminino'),
        ('N', 'Não especificado'),
    ]
    gender = models.CharField(max_length=1, choices=gender_choices, default='N')
    rescue_date = models.DateField()
    description = models.TextField()
    is_injured = models.BooleanField(default=False)
    observations = models.TextField(blank=True, null=True)
    is_vaccinated = models.BooleanField(default=False)

    class Meta:
        ordering = ['rescue_date']

class CatLifeguard(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField()
    date_of_birth = models.DateField()
    cat_quantity = models.PositiveSmallIntegerField()
    availability = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'