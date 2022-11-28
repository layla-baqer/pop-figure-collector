from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import PopFigure

from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .forms import EventForm

# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

# Sample data

# class PopFigure:
#   def __init__(self, character, franchise, category, feature, number):
#     self.character = character
#     self.franchise = franchise
#     self.category = category
#     self.feature = feature
#     self.number = number

# pop_figures_list = [
#   PopFigure('Charmander', 'Pokemon', 'Games', 'Metallic', 455),
#   PopFigure('Leafeon', 'Pokemon', 'Games', 'None', 866),
#   PopFigure('Ironheart', 'Black Panther', 'Marvel', 'None', 1176),
#   PopFigure('The Flash', 'The Flash', 'Television', 'Glow in the dark', 1097),
#   PopFigure('Eevee', 'Pokemon', 'Games', 'Glitter', 626)
# ]

def pop_figures_index(request):

    pop_figures_list = PopFigure.objects.all()

    return render(request, 'popfigures/index.html', {
        'popfigures': pop_figures_list
    })

def pop_figures_detail(request, pop_figure_id):

  pop_figure = PopFigure.objects.get(id=pop_figure_id)

  event_form = EventForm()

  return render(request, 'popfigures/detail.html', {
    'figure': pop_figure,
    'event_form': event_form
    })

def add_event(request, pop_figure_id):
    form = EventForm(request.POST)

    if form.is_valid():
        new_event = form.save(commit=False)
        new_event.popfigure_id = pop_figure_id
        new_event.save()
    
    return redirect('detail', pop_figure_id=pop_figure_id)

#######################################

class PopFigureCreate(CreateView):
    model = PopFigure
    fields = '__all__'
    success_url = '/popfigures/'

class PopFigureUpdate(UpdateView):
    model = PopFigure
    fields = '__all__'
    success_url = '/popfigures/'

class PopFigureDelete(DeleteView):
    model = PopFigure
    success_url = '/popfigures/'