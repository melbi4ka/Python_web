from django.shortcuts import render, redirect

from my_musicapp.web.forms import CreateProfileForm, AddAlbumForm, EditAlbumForm, DeleteAlbumForm, DeleteProfileForms
from my_musicapp.web.models import Profile, Album


def get_profile():
    profiles = Profile.objects.all()
    if profiles:
        return profiles[0]
    return None


def create_profile(request):
    if request.method == "GET":
        form = CreateProfileForm()
    else:
        form = CreateProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home index")
    context = {
        "form": form,
    }
    return render(request, "home-no-profile.html", context)


def home_index(request):
    profile = get_profile()
    albums = Album.objects.all()

    if not profile:
        return create_profile(request)

    context = {
        'profile': profile,
        'albums': albums,
    }
    return render(request, "home-with-profile.html", context)


def add_album(request):
    profile = get_profile()
    if request.method == "GET":
        form = AddAlbumForm()
    else:
        form = AddAlbumForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home index")
    context = {
        "form": form,
        "profile": profile,
    }
    return render(request, "add-album.html", context)


def details_album(request, pk):
    profile = get_profile()
    album = Album.objects.get(pk=pk)
    context = {
        "profile": profile,
        "album": album,
    }

    return render(request, "album-details.html", context)


def edit_album(request, pk):
    album = Album.objects.get(pk=pk)
    profile = get_profile()
    if request.method == "GET":
        form = EditAlbumForm(instance=album)
    else:
        form = EditAlbumForm(request.POST, instance=album)
        if form.is_valid():
            form.save()
            return redirect("home index")
    context = {
        "form": form,
        "album": album,
        "profile": profile,
    }
    return render(request, "edit-album.html", context)


def delete_album(request, pk):
    album = Album.objects.get(pk=pk)
    profile = get_profile()
    if request.method == "GET":
        form = DeleteAlbumForm(instance=album)
    else:
        form = DeleteAlbumForm(request.POST, instance=album)
        if form.is_valid():
            form.save()
            return redirect("home index")
    context = {
        "form": form,
        "album": album,
        "profile": profile,
    }
    return render(request, "delete-album.html", context)


def profile_details(request):
    profile = get_profile()
    albums = Album.objects.all()

    context = {
        "profile": profile,
        "albums": len(albums),
    }

    return render(request, "profile-details.html", context)


def delete_profiles(request):
    profile = get_profile()
    if request.method == "GET":
        form = DeleteProfileForms(instance=profile)
    else:
        form = DeleteProfileForms(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect("home index")
    context = {
        "form": form,
    }
    return render(request, "profile-delete.html", context)
