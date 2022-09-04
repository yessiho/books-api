from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=200)
    number_of_pages = models.IntegerField()
    publish_date = models.DateField()
    quantity = models.IntegerField()
    
    def __str__(self):
        return self.title