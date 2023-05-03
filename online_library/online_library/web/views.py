from collections import deque

from django.shortcuts import render, redirect

from online_library.web.forms import CreateProfileForm, AddBookForm, EditBookForm, EditProfileForm, DeleteProfileForm
from online_library.web.models import Profile, Book


def get_profile():
    profiles = Profile.objects.all()
    if profiles:
        return profiles[0]
    return None


def create_profile(request):
    if request.method == "GET":
        form = CreateProfileForm()
    else:
        form = CreateProfileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("home index")
    context = {
        "form": form,
    }
    return render(request, "home-no-profile.html", context)


# def home_index(request):
#     profile = get_profile()
#     book = Book.objects.all()
#     if not profile:
#         return redirect('create profile')
#
#     context = {
#         'profile': profile,
#         'book': book,
#     }
#     return render(request, "home-with-profile.html", context)
def home_index(request):
    profile = get_profile()
    book = Book.objects.all()
    rows = []
    per_row = 3

    for i in range(0, len(book), per_row):
        current_row = book[i: i + per_row]
        rows.append(current_row)

    if not profile:
        return redirect('create profile')

    context = {
        'profile': profile,
        'rows': rows,
    }
    return render(request, "home-with-profile.html", context)


def add_book(request):
    profile = get_profile()
    if request.method == "GET":
        form = AddBookForm()
    else:
        form = AddBookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home index")
    context = {
        "form": form,
        "profile": profile
    }

    return render(request, "add-book.html", context)


def edit_book(request, pk):
    profile = get_profile()
    book = Book.objects.get(pk=pk)
    if request.method == "GET":
        form = EditBookForm(instance=book)
    else:
        form = EditBookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect("home index")
    context = {
        "form": form,
        "book": book,
        "profile": profile,
    }
    return render(request, "edit-book.html", context)


def details_book(request, pk):
    profile = get_profile()
    book = Book.objects.get(pk=pk)
    context = {
        "book": book,
        "profile": profile,
    }

    return render(request, "book-details.html", context)


def delete_book(request, pk):
    book = Book.objects.get(pk=pk)
    book.delete()
    return redirect("home index")


def profile_page(request):
    profile = get_profile()

    context = {
        'profile': profile,
        "profile_str": str(profile)
    }

    return render(request, "profile.html", context)


def edit_profile(request):
    profile = get_profile()
    if request.method == "GET":
        form = EditProfileForm(instance=profile)
    else:
        form = EditProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect("profile page")
    context = {
        "form": form,
    }

    return render(request, "edit-profile.html", context)


def delete_profile(request):
    profile = get_profile()
    book = Book.objects.all()
    if request.method == "GET":
        form = DeleteProfileForm(instance=profile)
    else:
        form = DeleteProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect("home index")
    context = {
        "form": form,
        "profile": profile,
    }

    return render(request, "delete-profile.html", context)
