from .models import Pokemon, Evolution, Builds, HeldItems, BattleItems, BuildSkills, Skills, SkillUpgrades
from rest_framework import viewsets, generics
from .serializers import PokemonSerializer, EvolutionSerializer, BuildsSerializer, HeldItemsSerializer, BattleItemsSerializer, BuildSkillsSerializer, SkillsSerializer, SkillUpgradesSerializer
# Create your views here.


# class PokemonViewSet(viewsets.ModelViewSet):
#     queryset = Pokemon.objects.all()
#     serializer_class = PokemonSerializer


class PokemonList(generics.ListCreateAPIView):
    queryset = Pokemon.objects.all()
    serializer_class = PokemonSerializer


class PokemonDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Pokemon.objects.all()
    serializer_class = PokemonSerializer


# class EvolutionViewSet(viewsets.ModelViewSet):
#     queryset = Evolution.objects.all()
#     serializer_class = EvolutionSerializer


class EvolutionList(generics.ListCreateAPIView):
    queryset = Evolution.objects.all()
    serializer_class = EvolutionSerializer


class EvolutionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Evolution.objects.all()
    serializer_class = EvolutionSerializer


# class BuildsViewSet(viewsets.ModelViewSet):
# #     queryset = Builds.objects.all()
# #     serializer_class = BuildsSerializer


class BuildsList(generics.ListCreateAPIView):
    queryset = Evolution.objects.all()
    serializer_class = EvolutionSerializer


class BuildsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Builds.objects.all()
    serializer_class = BuildsSerializer


# class HeldItemsViewSet(viewsets.ModelViewSet):
#     queryset = HeldItems.objects.all()
#     serializer_class = HeldItemsSerializer


class HeldItemsList(generics.ListCreateAPIView):
    queryset = HeldItems.objects.all()
    serializer_class = HeldItemsSerializer


class HeldItemsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = HeldItems.objects.all()
    serializer_class = HeldItemsSerializer


# class BattleItemsViewSet(viewsets.ModelViewSet):
#     queryset = BattleItems.objects.all()
#     serializer_class = BattleItemsSerializer


class BattleItemsList(generics.ListCreateAPIView):
    queryset = BattleItems.objects.all()
    serializer_class = BattleItemsSerializer


class BattleItemsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = BattleItems.objects.all()
    serializer_class = BattleItemsSerializer


# class BuildSkillsViewSet(viewsets.ModelViewSet):
#     queryset = BuildSkills.objects.all()
#     serializer_class = BuildSkillsSerializer


class BuildSkillsList(generics.ListCreateAPIView):
    queryset = BuildSkills.objects.all()
    serializer_class = BuildSkillsSerializer


class BuildSkillsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = BuildSkills.objects.all()
    serializer_class = BuildSkillsSerializer


# class SkillsViewSet(viewsets.ModelViewSet):
#     queryset = Skills.objects.all()
#     serializer_class = SkillsSerializer


class SkillsList(generics.ListCreateAPIView):
    queryset = Skills.objects.all()
    serializer_class = SkillsSerializer


class SkillsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Skills.objects.all()
    serializer_class = SkillsSerializer


# class SkillUpgradesViewSet(viewsets.ModelViewSet):
#     queryset = SkillUpgrades.objects.all()
#     serializer_class = SkillUpgradesSerializer


class SkillUpgradesList(generics.ListCreateAPIView):
    queryset = SkillUpgrades.objects.all()
    serializer_class = SkillUpgradesSerializer


class SkillUpgradesDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = SkillUpgrades.objects.all()
    serializer_class = SkillUpgradesSerializer
