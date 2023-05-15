from rest_framework import serializers
from .models import Pokemon, Evolution, Builds, HeldItems, BattleItems, BuildSkills, Skills, SkillUpgrades


class BuildSkillsSerializer(serializers.ModelSerializer):
    class Meta:
        model = BuildSkills
        fields = '__all__'


class BattleItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = BattleItems
        fields = '__all__'


class HeldItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = HeldItems
        fields = '__all__'


class BuildsSerializer(serializers.ModelSerializer):
    held_items = HeldItemsSerializer(many=True, required=False)
    battle_itmes = BattleItemsSerializer(many=False, required=False)
    build_skills = BuildSkillsSerializer(many=True, required=False)

    class Meta:
        model = Builds
        fields = '__all__'


class SkillUpgradesSerializer(serializers.ModelSerializer):
    class Meta:
        model = SkillUpgrades
        fields = '__all__'


class SkillsSerializer(serializers.ModelSerializer):
    skill_upgrades = SkillUpgradesSerializer(many=True, required=False)

    class Meta:
        model = Skills
        fields = ('id', 'name', 'type', 'description', 'level', 'image', 'in_game_image', 'pokemon', 'skill_upgrades')


class EvolutionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evolution
        fields = '__all__'


class PokemonSerializer(serializers.ModelSerializer):
    evolution = EvolutionSerializer(many=True, required=False)
    builds = BuildsSerializer(many=True, required=False)
    skills = SkillsSerializer(many=True, required=False)

    class Meta:
        model = Pokemon
        fields = ('id', 'name', 'difficulty', 'role',
                  'image', 'evolution', 'builds', 'skills')
