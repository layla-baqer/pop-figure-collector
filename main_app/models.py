from django.db import models

# Create your models here.

class PopFigure(models.Model):
    character = models.CharField(max_length=100)
    franchise = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    feature = models.CharField(max_length=100)
    number = models.IntegerField()

    def __str__(self):
        return self.character