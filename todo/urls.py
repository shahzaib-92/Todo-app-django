from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('delete/<id>', views.delete, name="delete"),
    path('check/<id>', views.check, name="check"),
    path('uncheck/<id>', views.uncheck, name="uncheck"),
    path('edit/<id>', views.edit, name="edit")
]
