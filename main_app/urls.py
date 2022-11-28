from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('about/', views.about),
    path('popfigures/', views.pop_figures_index, name='index'),
    path('popfigures/<int:pop_figure_id>/', views.pop_figures_detail, name='detail')
]