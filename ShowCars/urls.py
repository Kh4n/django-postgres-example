from django.urls import path
from ShowCars import views

urlpatterns = [
    path("api/get_cars", views.get_cars),
    path("view_cars", views.view_cars)
]
