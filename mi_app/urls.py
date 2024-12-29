# mi_app/urls.py
from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    
    path('menosstock/',views.reducirSTOCK, name= 'restarstock'),
 
]