from django.urls import path
from .views import api_list_hats, api_show_hats

urlpatterns = [
    path("hats/", api_list_hats, name="api_list_hats"),
    path("location/<int:location_vo_id>/hat", api_show_hats, name="api_show_hats"),
    path("hats/<int:id>/", api_show_hats, name="api_show_hats"),
]
