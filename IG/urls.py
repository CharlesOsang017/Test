from . import views
from django.urls import path


urlpatterns = [
    path('',views.home, name='Ig-home' ),
    path('about',views.about, name='Ig-about' ),


]
