from django.shortcuts import render, redirect

from notes_examtask.web.forms import CreateProfileForm, AddNoteForm, EditNoteForm, DeleteNoteForm
from notes_examtask.web.models import Profile, Note


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
    note = Note.objects.all()

    if not profile:
        return redirect('create profile')

    context = {
        'profile': profile,
        'note': note,
    }
    return render(request, "home-with-profile.html", context)


def add_note(request):
    note = Note.objects.all()
    if request.method == "GET":
        form = AddNoteForm()
    else:
        form = AddNoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home index")
    context = {
        "form": form,
        "note": note,
    }
    return render(request, "note-create.html", context)


def edit_note(request, pk):
    note = Note.objects.get(pk=pk)
    if request.method == "GET":
        form = EditNoteForm(instance=note)
    else:
        form = EditNoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect("home index")
    context = {
        "form": form,
        "note": note,
    }
    return render(request, "note-edit.html", context)


def delete_note(request, pk):
    note = Note.objects.get(pk=pk)
    if request.method == "GET":
        form = DeleteNoteForm(instance=note)
    else:
        form = DeleteNoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect("home index")
    context = {
        "form": form,
        "note": note,
    }
    return render(request, "note-delete.html", context)


def details_note(request, pk):
    note = Note.objects.get(pk=pk)
    context = {
        "note": note,
    }

    return render(request, "note-details.html", context)


def profile_page(request):
    profile = Profile.objects.first()
    str_profile = str(profile)
    notes = Note.objects.all()
    len_notes = len(notes)
    context = {
        "profile": profile,
        "str_profile": str_profile,
        "len_notes": len_notes,
    }
    return render(request, "profile.html", context)


def profile_delete(request):
    user_profile = Profile.objects.first()
    all_notes = Note.objects.all()

    user_profile.delete()
    all_notes.delete()
    return redirect('home index')

