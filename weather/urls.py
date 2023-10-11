from django.urls import path
from .views import weather_query_view

urlpatterns = [
    path("query", weather_query_view, name="weather_query"),
]
