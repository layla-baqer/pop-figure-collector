from django.db import models

# Create your models here.

Locations = (
    ('B', 'Bahrain'),
    ('D', 'Dubai'),
    ('S', 'Saudi Arabia'),
    ('Q', 'Qatar'),
    ('K', 'Kuwait')
)

class PopFigure(models.Model):
    character = models.CharField(max_length=100)
    franchise = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    feature = models.CharField(max_length=100)
    number = models.IntegerField()

    def __str__(self):
        return self.character

class Event(models.Model):
    # 'Event Date' will be the input field label, if it's not written then it will be same as the column name
    date = models.DateField('Event Date')
    location = models.CharField(
        max_length=1,
        choices=Locations,
        default=Locations[0][0]
    )
    popfigure = models.ForeignKey(PopFigure, on_delete=models.CASCADE)

    def __str__(self):
        return (f"Participated at {self.get_location_display()} on {self.date}")