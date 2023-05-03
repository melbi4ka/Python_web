
from django.urls import path, include

from online_library.web.views import home_index, add_book, edit_book, details_book, profile_page, edit_profile, \
    delete_profile, create_profile, delete_book

urlpatterns = (
    path("", home_index, name="home index"),
    path("add/", add_book, name="add book"),
    path("edit/<pk>/", edit_book, name="edit book"),
    path("details/<pk>/", details_book, name="details book"),
    path("delete/<pk>", delete_book, name="delete book"),
    path("profile/", include([
        path("", profile_page, name="profile page"),
        path("edit/", edit_profile, name="edit profile"),
        path("delete/", delete_profile, name="delete profile"),
        path("create/", create_profile, name="create profile"),
    ]))
)
