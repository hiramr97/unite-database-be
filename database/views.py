from django.shortcuts import render
from .models import Pokemon, Evolution
from rest_framework import viewsets
from .serializers import PokemonSerializer, EvolutionSerializer

# Create your views here.
class PokemonViewSet(viewsets.ModelViewSet):
    queryset = Pokemon.objects.all()
    serializer_class = PokemonSerializer

class EvolutionViewSet(viewsets.ModelViewSet):
    queryset = Evolution.objects.all()
    serializer_class = EvolutionSerializer