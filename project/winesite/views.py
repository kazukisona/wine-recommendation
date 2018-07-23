from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
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
    queryset = WineTable.objects.all()[:10]
    serializer_class = WineTableSerializer

# templates
def wine_list(request):
    wines = WineTable.objects.all()[:10]
    return render(request, 'wine_list.html', {'wines': wines})

