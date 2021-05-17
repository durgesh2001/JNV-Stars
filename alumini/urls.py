from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="index"),
    path('alumini/', views.alumini, name="alumini"),
    path('about/', views.about, name="about"),
    path('campus/', views.campus, name="campus"),
    path('contact/', views.contact, name="contact"),
   
]
