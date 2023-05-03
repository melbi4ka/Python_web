from django.urls import path

from notes_examtask.web.views import home_index, add_note, edit_note, delete_note, details_note, profile_page, \
    create_profile, profile_delete

urlpatterns = (
    path("", home_index, name="home index"),
    path("create/", create_profile, name="create profile"),
    path("add/", add_note, name="add note"),
    path("edit/<pk>/", edit_note, name="edit note"),
    path("delete/<pk>/", delete_note, name="delete note"),
    path("details/<pk>/", details_note, name="details note"),
    path("profile/", profile_page, name="profile page"),
    path("profile/delete/", profile_delete, name="profile delete"),
)
