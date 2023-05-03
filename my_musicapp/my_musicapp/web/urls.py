from django.urls import include, path

from my_musicapp.web.views import home_index, add_album, details_album, edit_album, delete_album, \
    delete_profiles, profile_details, create_profile

urlpatterns = (
    path("", home_index, name="home index"),
    path("album/", include([
        path("add/", add_album, name="add album"),
        path("details/<int:pk>/", details_album, name="details album"),
        path("edit/<int:pk>/", edit_album, name="edit album"),
        path("delete/<int:pk>/", delete_album, name="delete album"),
    ])),
    path("profile/", include([
        path("details/", profile_details, name="profile_details"),
        path("delete/", delete_profiles, name="delete profiles"),
    ])),
)