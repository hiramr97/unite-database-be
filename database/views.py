from django.shortcuts import render
from .models import Pokemon, Evolution, Builds, HeldItems, BattleItems, BuildSkills
from rest_framework import viewsets
from .serializers import PokemonSerializer, EvolutionSerializer, BuildsSerializer, HeldItemsSerializer, BattleItemsSerializer, BuildSkillsSerializer

# Create your views here.
class PokemonViewSet(viewsets.ModelViewSet):
    queryset = Pokemon.objects.all()
    serializer_class = PokemonSerializer

class EvolutionViewSet(viewsets.ModelViewSet):
    queryset = Evolution.objects.all()
    serializer_class = EvolutionSerializer

class BuildsViewSet(viewsets.ModelViewSet):
    queryset = Builds.objects.all()
    serializer_class = BuildsSerializer

class BuildsViewSet(viewsets.ModelViewSet):
    queryset = Builds.objects.all()
    serializer_class = BuildsSerializer

class HeldItemsViewSet(viewsets.ModelViewSet):
    queryset = HeldItems.objects.all()
    serializer_class = HeldItemsSerializer

class BattleItemsViewSet(viewsets.ModelViewSet):
    queryset = BattleItems.objects.all()
    serializer_class = BattleItemsSerializer

class BuildSkillsViewSet(viewsets.ModelViewSet):
    queryset = BuildSkills.objects.all()
    serializer_class = BuildSkillsSerializer