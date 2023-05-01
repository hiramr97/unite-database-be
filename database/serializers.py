from rest_framework import serializers
from .models import Pokemon, Evolution


class EvolutionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evolution
        fields = '__all__'


class PokemonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pokemon
        fields = '__all__'
        evolution = EvolutionSerializer(many=True, required=False)
