from django.shortcuts import render, redirect

from examtask.web.forms import CreateProfileForm, CreateCarForm, CarEditForm, CarDeleteForm, ProfileEditForm, \
    ProfileDeleteForm
from examtask.web.models import Profile, Car


def get_profile():
    profiles = Profile.objects.all()
    if profiles:
        return profiles[0]
    return None


def home_index(request):
    profile = get_profile()

    context = {
        'profile': profile,

    }
    return render(request, "index.html", context)


def create_profile(request):
    if request.method == "GET":
        form = CreateProfileForm()
    else:
        form = CreateProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("catalogue create")
    context = {
        "form": form,
    }
    return render(request, "profile-create.html", context)


def catalogue_create(request):
    profile = get_profile()
    cars = Car.objects.all()
    context = {
        "cars": cars,
        "len_cars": len(cars),
        "profile": profile,
    }

    return render(request, "catalogue.html", context)


def create_car(request):
    profile = get_profile()

    if request.method == "GET":
        form = CreateCarForm()
    else:
        form = CreateCarForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("catalogue create")
    context = {
        "form": form,
        "profile": profile,
    }
    return render(request, "car-create.html", context)


def car_details(request, pk):
    car = Car.objects.get(pk=pk)
    profile = get_profile()
    context = {
        "car": car,
        "profile":profile,
    }

    return render(request, "car-details.html", context)


def car_edit(request, pk):
    profile = get_profile()
    car = Car.objects.get(pk=pk)
    if request.method == "GET":
        form = CarEditForm(instance=car)
    else:
        form = CarEditForm(request.POST, instance=car)
        if form.is_valid():
            form.save()
            return redirect("catalogue create")
    context = {
        "form": form,
        "profile": profile,
        "car": car,
        "pk": pk,
    }
    return render(request, "car-edit.html", context)


def delete_car(request, pk):
    profile = get_profile()
    car = Car.objects.get(pk=pk)
    if request.method == "GET":
        form = CarDeleteForm(instance=car)
    else:
        form = CarDeleteForm(request.POST, instance=car)
        if form.is_valid():
            form.save()
            return redirect("catalogue create")
    context = {
        "form": form,
        "profile": profile,
        "car": car,
        "pk": pk,
    }
    return render(request, "car-delete.html", context)




def details_profile(request):
    profile = get_profile()
    cars = Car.objects.all()
    context = {
        "profile": profile,
        "full_name": profile.full_name,
        "sum_cars": sum([car.price for car in cars]),
    }

    return render(request, "profile-details.html", context)


def edit_profile(request):
    profile = get_profile()

    if request.method == "GET":
        form = ProfileEditForm(instance=profile)
    else:
        form = ProfileEditForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect("catalogue create")
    #    wrong redirect - valid is details_profile
    context = {
        "form": form,
        "profile": profile,
    }
    return render(request, "profile-edit.html", context)


def delete_profile(request):
    profile = get_profile()

    if request.method == "GET":
        form = ProfileDeleteForm(instance=profile)
    else:
        form = ProfileDeleteForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect("home index")
    context = {
        "form": form,
        "profile": profile,
    }

    return render(request, "profile-delete.html", context)
