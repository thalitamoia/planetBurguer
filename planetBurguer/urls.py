from django.urls import path
from planetBurguer import views
urlpatterns = [
    path('', views.burguerindex),
]
