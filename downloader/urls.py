from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('auto/<magnet_link>', views.auto, name="auto"),
]