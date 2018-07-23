from rest_framework import serializers
from winesite.models import Wine, User, WineTable

class WineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wine
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__' # test including password

class WineTableSerializer(serializers.ModelSerializer):
    class Meta:
        model = WineTable
        fields = '__all__'