
from django.urls import path

from recipes.web.views import home_index, create_recipe, edit_recipe, delete_recipe, details_recipe

urlpatterns = (
    path("", home_index, name="home index"),
    path("create/", create_recipe, name="create recipe"),
    path("edit/<int:pk>/", edit_recipe, name="edit recipe"),
    path("delete/<int:pk>/", delete_recipe, name="delete recipe"),
    path("details/<int:pk>/", details_recipe, name="details recipe"),
)
