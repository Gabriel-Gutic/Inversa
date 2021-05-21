from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.matrix, name='Home-page'),
    path('determinant_dim=<n>', views.det, name='Det-page'),
    path('inversa_dim=<n>', views.inversa, name='Inversa-page'),
]