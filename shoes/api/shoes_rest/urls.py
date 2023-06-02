from django.urls import path

from .views import shoes_list, show_shoe


urlpatterns = [
    path("shoes/", shoes_list, name="shoes_list"),
    path("shoes/<int:id>/", show_shoe, name="show_shoe"),
]
