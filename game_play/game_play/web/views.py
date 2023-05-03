from django.shortcuts import render, redirect

from game_play.web.forms import CreateProfileForms, EditProfileForms, DeleteProfileForms, CreateGameForm, EditGameForm, \
    DeleteGameForm
from game_play.web.models import Profile, Game


def get_profile():
    profiles = Profile.objects.all()
    if profiles:
        return profiles[0]
    return None


def home_index(request):
    profile = get_profile()
    have_profile = True

    if not profile:
        have_profile = False

    context = {
        "profile": profile,
        "have_profile": have_profile,
    }

    return render(request, "home-page.html", context)


def dashboard_index(request):
    profile = get_profile()
    game = Game.objects.all()

    context = {
        'profile': profile,
        'game': game,
    }
    return render(request, "dashboard.html", context)


def create_profile(request):
    if request.method == "GET":
        form = CreateProfileForms()
    else:
        form = CreateProfileForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home index")
    context = {
        "form": form,
        # "no_profile": True,
    }
    return render(request, "create-profile.html", context)


def details_profile(request):
    profile = get_profile()
    if not profile:
        return redirect("create profile")


    game = Game.objects.all()
    all_games = len(game)
    if all_games > 0:
        average_rating = sum(g for g in game) / all_games
    else:
        average_rating = f"0.0"
    context = {
        "profile": profile,
        "all_games": all_games,
        "average_rating": average_rating,

    }
    return render(request, "details-profile.html", context)


def edit_profile(request):
    profile = get_profile()
    if request.method == "GET":
        form = EditProfileForms(instance=profile)
    else:
        form = EditProfileForms(request.POST, instance=profile)
        # form.full_clean()
        if form.is_valid():
            form.save()
            return redirect("details profile")
    context = {
        "form": form,
        "profile": profile,
    }
    return render(request, "edit-profile.html", context)


def delete_profile(request):
    profile = get_profile()
    if request.method == "GET":
        form = DeleteProfileForms(instance=profile)
    else:
        form = DeleteProfileForms(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect("home index")
    context = {
        "form": form,
        "profile": profile,
    }
    return render(request, "delete-profile.html", context)


def create_game(request):
    if request.method == "GET":
        form = CreateGameForm()
    else:
        form = CreateGameForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("dashboard index")
    context = {
        "form": form,
    }
    return render(request, "create-game.html", context)


def details_game(request, pk):
    game = Game.objects.get(pk=pk)
    profile = get_profile()
    context = {
        "profile": profile,
        "game": game,
    }
    return render(request, "details-game.html", context)


def edit_game(request, pk):
    game = Game.objects.get(pk=pk)
    if request.method == "GET":
        form = EditGameForm(instance=game)
    else:
        form = EditGameForm(request.POST, instance=game)
        if form.is_valid():
            form.save()
            return redirect("dashboard index")
    context = {
        "form": form,
        "game": game,
    }
    return render(request, "edit-game.html", context)


def delete_game(request, pk):
    game = Game.objects.get(pk=pk)
    if request.method == "GET":
        form = DeleteGameForm(instance=game)
    else:
        form = DeleteGameForm(request.POST, instance=game)
        if form.is_valid():
            form.save()
            return redirect("dashboard index")
    context = {
        "form": form,
        "game": game,
    }

    return render(request, "delete-game.html", context)
