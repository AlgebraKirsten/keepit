from django.urls import path

from . import views

urlpatterns = [
    path('release_me', views.release_me, name='release'),
]