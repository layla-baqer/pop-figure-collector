from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('about/', views.about),
    path('popfigures/', views.pop_figures_index, name='index'),
    path('popfigures/<int:pop_figure_id>/', views.pop_figures_detail, name='detail'),
    path('popfigures/create/', views.PopFigureCreate.as_view(), name='pop_figure_create'),
    path('popfigures/<int:pk>/update/', views.PopFigureUpdate.as_view(), name='pop_figure_update'),
    path('popfigures/<int:pk>/delete/', views.PopFigureDelete.as_view(), name='pop_figure_delete'),
    path('popfigures/<int:pop_figure_id>/add_event/', views.add_event, name='add_event')
]