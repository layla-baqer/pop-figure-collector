from django.contrib import admin

from .models import PopFigure
from .models import Event

# Register your models here.

admin.site.register(PopFigure)
admin.site.register(Event)