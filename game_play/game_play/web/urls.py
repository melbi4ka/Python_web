
from django.urls import path

from game_play.web.views import home_index, dashboard_index, create_profile, details_profile, edit_profile, \
    delete_profile, create_game, details_game, edit_game, delete_game

urlpatterns = (
    path("", home_index, name= "home index"),
    path("dashboard/", dashboard_index, name="dashboard index"),
    path("profile/create/", create_profile, name="create profile"),
    path("profile/details/", details_profile, name="details profile"),
    path("profile/edit/", edit_profile, name="edit profile"),
    path("profile/delete/", delete_profile, name="delete profile"),
    path("game/create/", create_game, name="create game"),
    path("game/details/<pk>/", details_game, name="details game"),
    path("game/edit/<pk>/", edit_game, name="edit game"),
    path("game/delete/<pk>/", delete_game, name="delete game"),
)