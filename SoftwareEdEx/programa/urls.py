from django.urls import path
from . import views

#app_name = 'programa'

urlpatterns = [
    path('view', views.view_programa , name='view_programa'),
    path('add', views.add_programa, name='add_programa'),
    path('save', views.save_programa, name='save_programa'),
    path('programa/edit/<int:pk>/', views.edit_programa, name='edit_programa'),
    path('programa/modulo/<int:pk>/edit/', views.edit_modulo, name='edit_modulo'),
    path('programa/sesion/<int:pk>/edit/', views.edit_sesion, name='edit_sesion'),
]
