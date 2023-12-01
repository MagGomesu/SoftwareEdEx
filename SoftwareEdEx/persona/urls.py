from django.urls import path
from .views import dashboard_view, edit_estudiante_view, delete_estudiante_view

urlpatterns = [
    path('dashboard/', dashboard_view, name='dashboard'),
    path('edit-estudiante/<int:id>/', edit_estudiante_view, name='edit_estudiante'),
    path('delete-estudiante/<int:id>/', delete_estudiante_view, name='delete_estudiante'),
]
