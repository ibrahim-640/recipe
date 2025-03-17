from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout
from . forms import RecipeForm, Recipe, registerForm


def search_recipes(request):
    query = request.GET.get('q', '')  # Get search input
    recipes = Recipe.objects.filter(title__icontains=query) if query else []

    return render(request, 'search_results.html', {'recipes': recipes, 'query': query})

    # Home - List all recipes
def recipe_list(request):
    recipes = Recipe.objects.all()
    return render(request, 'recipe_list.html', {'recipes': recipes})

def register_user(request):
    if request.method == "POST":
        form = registerForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('list')

    else:

        form=registerForm()
    return render(request, 'register.html',context={'form':form})
# View Recipe Details
def recipe_detail(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    return render(request, 'recipe_detail.html', {'recipe': recipe})

def login_user(request):
    if request.method == "POST":
      form = AuthenticationForm(data=request.POST)
      if form.is_valid():
          user =form.get_user()
          login(request, user)
          return redirect('list')
    else:
      form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def logout_user(request):
    logout(request)
    return redirect('login')

# Create Recipe
@login_required
def recipe_create(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.author = request.user
            recipe.save()
            return redirect('list')
    else:
        form = RecipeForm()
    return render(request, 'recipe_form.html', {'form': form})


# Update Recipe
@login_required
def recipe_update(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    if request.user != recipe.author:
        return redirect('list')

    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES, instance=recipe)
        if form.is_valid():
            form.save()
            return redirect('list')
    else:
        form = RecipeForm(instance=recipe)
    return render(request, 'recipe_form.html', {'form': form})


# Delete Recipe
@login_required
def recipe_delete(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    if request.user == recipe.author:
        recipe.delete()
    return redirect('list')


