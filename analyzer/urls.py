from django.urls import path
from . import views

urlpatterns = [

    path("", views.home),

    path("districts/", views.district_data),

    path("analyze/", views.analyze),

    path("village/", views.village),

    path("forecast/", views.forecast),

]