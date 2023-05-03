
from django.urls import path

from examtask.web.views import home_index, create_profile, catalogue_create, create_car, car_details, car_edit, \
    delete_car, details_profile, edit_profile, delete_profile

urlpatterns =(
    path('', home_index, name="home index"),
    path('profile/create/', create_profile, name="create profile"),
    path('catalogue/', catalogue_create, name="catalogue create"),
    path('car/create/', create_car, name="create car"),
    path('car/<int:pk>/details/', car_details, name="car details"),
    path('car/<int:pk>/edit/', car_edit, name="car edit"),
    path('car/<int:pk>/delete/', delete_car, name="car delete"),
    path('profile/details/', details_profile, name="details profile"),
    path('profile/edit/', edit_profile, name="edit profile"),
    path('profile/delete/', delete_profile, name="delete profile"),


)
