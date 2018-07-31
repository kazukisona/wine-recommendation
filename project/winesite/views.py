from django.shortcuts import render
from django.db.models import Q

# Create your views here.
from winesite.models import Wine, User, WineTable
from winesite.serializers import WineSerializer, UserSerializer, WineTableSerializer
from rest_framework import generics

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

def wine_list(request):
    wines = WineTable.objects.all()
    return render(request, 'wine_list.html', {'wines': wines})

def recommendation(request):
    if request.method == "POST":
        # get values from form
        w_type = request.POST.getlist('type')[0]
        region = request.POST.getlist('region')[0]
        vintage = request.POST.getlist('vintage')[0]

        # filter wines based on the answers
        # if wine is non-vintage
        if vintage != 'nv':
            wines = (WineTable.objects.exclude(vintage='nv')
                                      .filter(type=w_type)
                                      .filter(country__in=region_list(region)))
        else:
            wines = (WineTable.objects.filter(type=w_type)
                                      .filter(vintage=vintage)
                                      .filter(country__in=region_list(region)))

    return render(request, 'recommendation.html', {'wines': wines})

def selector(request):
    return render(request, 'selector.html')

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
