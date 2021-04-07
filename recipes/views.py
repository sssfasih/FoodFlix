from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib.auth.decorators import login_required
from .models import User,Category, Recipe


# Create your views here.


def index(request):
    print("123213213213213")
    latest = Recipe.objects.all().order_by('Created')
    print(latest)
    print("123213213213213")
    return render(request, 'recipes/index.html',{'recipes':latest})


def category(request, cat):
    print("*****----******")
    print("*****----******")

    cats = []
    for eachCat in Category.objects.all():
        cats.append(eachCat.Name.lower())

    if cat.lower() in cats:
        recipes = Recipe.objects.filter(category__Name=cat.title())
        print("***********")
        print(recipes)
        print("***********")
    else:
        recipes = Recipe.objects.none()

    print("*****----******")
    print("*****----******")

    return render(request, 'recipes/category.html', {'category': cat.title(),'recipes':recipes})

def view_recipe(request,name):
    recipe_obj = Recipe.objects.get(pk=5)

    return render(request,'recipes/view_recipe.html',{'recipe':recipe_obj})



def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "recipes/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse("index"))
        return render(request, "recipes/login.html")

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def signup(request):
    if request.method == "POST":
        name = request.POST["Name"]
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "recipes/signup.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password, first_name=name)
            user.save()
        except IntegrityError:
            return render(request, "recipes/signup.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "recipes/signup.html")
