from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse,HttpResponseBadRequest,HttpResponseNotAllowed
from django.contrib.auth.decorators import login_required
from .models import User,Category, Recipe,RecipeImage
from markdown2 import markdown
from django.utils.text import slugify

# Create your views here.


def index(request):

    latest = Recipe.objects.all().order_by('Created')

    return render(request, 'recipes/index.html',{'recipes':latest})


def category(request, cat):

    cats = []
    for eachCat in Category.objects.all():
        cats.append(eachCat.Name.lower())

    if cat.lower() in cats:
        recipes = Recipe.objects.filter(Tags__Name__contains=cat.title())
        cat_obj = Category.objects.get(Name__contains=cat.lower())
        print("***********")
        print(cat_obj)
        print("***********")
        if cat_obj.Name == 'lunch':
            cat_obj.Name = "Lunch/Dinner"
    else:
        recipes = Recipe.objects.none()
        cat_obj = Category.objects.none()


    return render(request, 'recipes/category.html', {'category': cat_obj,'recipes':recipes})

def view_recipe(request,name):
    name = name.replace("-",' ').strip().lower()
    check = name.replace(' ','')
    if check.isalnum():
        print("alphabet")
    else:return HttpResponseRedirect(reverse('all_category'))

    print("78787878787")
    print(name)
    print("78787878787")
    recipe_obj = Recipe.objects.get(Name=name)
    ingredients = markdown(recipe_obj.Ingredients)
    method = markdown(recipe_obj.Directions)
    images = recipe_obj.images.all()
    print(images)

    return render(request,'recipes/view_recipe.html',{'recipe':recipe_obj,'ingredients':ingredients,'method':method,'img_objs':images})

def all_categories(request):
    return HttpResponse('ALL CATEGORIES PAGE')

def add_recipe(request):
    cats = (cat.Name for cat in Category.objects.all())
    if request.method == 'POST':

        name = request.POST.get('name').strip().lower()
        slug = slugify(name)
        ingredients = request.POST.get('ingredients').strip().lower()
        method = request.POST.get('method').strip().lower()
        files = request.FILES.getlist('uploaded_images')
        if name=="" or ingredients == "" or method == "":
            print("BLANK DATA")

        else:
            new_rec = Recipe(Name=name,Ingredients=ingredients,Directions=method,Posted_by=request.user,Slug=slug)
            new_rec.save()
            for loop in files:
                img = RecipeImage(recipe=new_rec, image=loop)
                img.save()
            for loop in cats:
                if request.POST.get(loop) == "True":
                    cat_obj = Category.objects.get(Name=loop)
                    new_rec.Tags.add(cat_obj)



    return render(request,'recipes/add_recipe.html',{'cats':cats})

@login_required
def view_profile(request, id):
    requested_user = User.objects.get(pk=id)
    if requested_user != request.user:
        HttpResponseRedirect(reverse('index'))
    # print(request.user,' != ',followers)
    #r = request.GET.get('page')

    #p = Paginator(posts, 10)

    #if r:
    #    page_posts = p.page(r)
    #else:
    #    page_posts = p.page(1)

    return render(request, 'recipes/view_profile.html')


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
