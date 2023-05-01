from rest_framework import serializers
from .models import Pokemon, Evolution, Builds, HeldItems

class HeldItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = HeldItems
        fields = '__all__'


class BuildsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Builds
        fields = '__all__'
        held_items = HeldItemsSerializer(many=True, required=False)


class EvolutionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evolution
        fields = '__all__'


class PokemonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pokemon
        fields = '__all__'
        evolution = EvolutionSerializer(many=True, required=False)
        builds = BuildsSerializer(many=True, required=False)
