from django.shortcuts import render, redirect
from django.db.models import Q

# Create your views here.
from winesite.models import Wine, User, WineTable
from winesite.serializers import WineSerializer, UserSerializer, WineTableSerializer
from rest_framework import generics
from django.contrib.auth import authenticate

# Create your views here.
# Serializer
class WineListCreate(generics.ListCreateAPIView):
    queryset = Wine.objects.all()
    serializer_class = WineSerializer

class UserListCreate(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class WineTableListCreate(generics.ListCreateAPIView):
    queryset = WineTable.objects.all()[1:11]
    serializer_class = WineTableSerializer

# templates
def index(request):
    return render(request, 'index.html')

def signup(request):
    return render(request, 'signUp.html')

def login(request):
    return render(request, 'login.html')

def recommendation(request):
    if request.method == "POST":
        # get values from form
        w_type = request.POST.getlist('type')[0]
        region = request.POST.getlist('region')[0]
        vintage = request.POST.getlist('vintage')[0]

        # filter wines based on the answers
        # if wine is vintage
        if vintage != 'nv':
            wines = (WineTable.objects.exclude(vintage='nv')
                                      .filter(type=w_type)
                                      .filter(country__in=region_list(region)))
        else:
            wines = (WineTable.objects.filter(type=w_type)
                                      .filter(vintage=vintage)
                                      .filter(country__in=region_list(region)))

    return render(request, 'selections.html', {'wines': wines})

def selector(request):
    return render(request, 'selector.html')

# Create new user from signup.htlm
# Add user to the user table winesite_user
def new_user(request):
    if request.method == "POST":
        # get values from the sign in form

        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        password = request.POST.get('password')
        birthday = request.POST.get('birthday')

        new_user = User(firstname=firstname,lastname=lastname,email=email,password=password,birthday=birthday)
        new_user.save()

    
    return redirect('selector')

def user_auth(request):
    if request.method == "POST":

        # get values from login form and authenticate with database

        email = request.POST.get('exampleInputEmail1')
        password = request.POST.get('exampleInputPassword1')
        user = User.objects.filter(email=email).filter(password=password)
        
        if user is not None: 
            return render(request, 'profile.html')      

    return redirect('login') 



# helper function
def region_list(region_name):
    countries = {
        "Africa": ["South Africa"],
        "North America": ["USA", "Canada"],
        "South America": ["Mexico", "Chile", "Argentina"],
        "Oseania": ["Australia", "New Zealand"],
        "Western Europe": ["France", "Germany", "Austria"],
        "Southern Europe": ["Spain", "Portugal", "Italy", "Greece"],
        "Eastern Europe": ["Croatia", "Hungary", "Serbia", "Slovenia", "Ukraine", "Su", "Turkey"],
        "United Kingdom": ["UK", "Wales"],
    }

    return countries[region_name]
