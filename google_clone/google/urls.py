from django.urls import path

from . import views
from .views import search


urlpatterns = [
    path('', views.home),
    path('search', views.search, name='search')
]