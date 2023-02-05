from django.db import models

# Create your models here.
class Car(models.Model):
    name = models.CharField(max_length = 100)
    year_of_release = models.DateField()
    manufacturer = models.CharField(max_length= 100)
    horsepower = models.IntegerField()
    image_url = models.URLField(max_length=200, null=True)
    def __str__(self):
        return self.name
    