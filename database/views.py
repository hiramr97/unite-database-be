from .models import Pokemon, Evolution, Builds, HeldItems, BattleItems, BuildSkills, Skills, SkillUpgrades
from rest_framework import viewsets
from .serializers import PokemonSerializer, EvolutionSerializer, BuildsSerializer, HeldItemsSerializer, BattleItemsSerializer, BuildSkillsSerializer, SkillsSerializer, SkillUpgradesSerializer

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


class SkillsViewSet(viewsets.ModelViewSet):
    queryset = Skills.objects.all()
    serializer_class = SkillsSerializer


class SkillUpgradesViewSet(viewsets.ModelViewSet):
    queryset = SkillUpgrades.objects.all()
    serializer_class = SkillUpgradesSerializer
