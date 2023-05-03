from django.shortcuts import render, redirect

from recipes.web.forms import CreateRecipeForm, EditRecipeForm, DeleteRecipeForm
from recipes.web.models import Recipe


def get_recipes():
    recipe = Recipe.objects.all()
    if recipe:
        return recipe[0]
    return None


def home_index(request):
    recipes = Recipe.objects.all()
    context = {
        "recipes": recipes,
    }

    return render(request, "index.html", context)


def create_recipe(request):
    if request.method == "GET":
        form = CreateRecipeForm()
    else:
        form = CreateRecipeForm(request.POST, )
        if form.is_valid():
            form.save()
            return redirect("home index")
    context = {
        "form": form,
    }
    return render(request, "create.html", context)


def edit_recipe(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    if request.method == "GET":
        form = EditRecipeForm(instance=recipe)
    else:
        form = EditRecipeForm(request.POST,instance=recipe)
        if form.is_valid():
            form.save()
            return redirect("home index")
    context = {
        "form": form,
        "recipe": recipe,
    }
    return render(request, "edit.html", context)


def delete_recipe(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    if request.method == "GET":
        form = DeleteRecipeForm(instance=recipe)
    else:
        form = DeleteRecipeForm(request.POST, instance=recipe)
        if form.is_valid():
            form.save()
            return redirect("home index")
    context = {
        "form": form,
        "recipe": recipe,
    }
    return render(request, "delete.html", context)


def details_recipe(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    context = {
        "recipe": recipe,
        "ingrеdients": recipe.ingredients.split(", "),
    }

    return render(request, "details.html", context)
