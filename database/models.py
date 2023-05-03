from django.db import models


class Pokemon(models.Model):
    name = models.CharField(max_length=21)
    difficulty = models.CharField(max_length=21)
    role = models.CharField(max_length=21)
    image = models.TextField()


class Evolution(models.Model):
    pokemon = models.ForeignKey(
        Pokemon, on_delete=models.CASCADE, related_name='evolution')
    name = models.CharField(max_length=21)
    level = models.CharField(max_length=7)
    image = models.TextField()


class Builds(models.Model):
    pokemon = models.ForeignKey(
        Pokemon, on_delete=models.CASCADE, related_name='builds')
    name = models.CharField(max_length=21)
    lane = models.CharField(max_length=7)


class HeldItems(models.Model):
    build = models.ForeignKey(
        Builds, on_delete=models.CASCADE, related_name='held_items')
    name = models.CharField(max_length=21)
    image = models.TextField()


class BattleItems(models.Model):
    build = models.ForeignKey(
        Builds, on_delete=models.CASCADE, related_name='battle_items')
    name = models.CharField(max_length=21)
    image = models.TextField()
    optional_name = models.CharField(max_length=21)
    optional_image = models.TextField()


class BuildSkills(models.Model):
    build = models.ForeignKey(
        Builds, on_delete=models.CASCADE, related_name='build_skills')
    name = models.CharField(max_length=21)
    image = models.TextField()
    level = models.CharField(max_length=7)


class Skills(models.Model):
    pokemon = models.ForeignKey(
        Pokemon, on_delete=models.CASCADE, related_name='skills')
    name = models.CharField(max_length=50)
    type = models.CharField(max_length=21)
    description = models.TextField()
    level = models.CharField(max_length=21, null=True, blank=True)
    image = models.TextField(null=True, blank=True)
    in_game_image = models.TextField(null=True, blank=True)


class SkillUpgrades(models.Model):
    skill = models.ForeignKey(
        Skills, on_delete=models.CASCADE, related_name='skill_upgrades')
    name = models.CharField(max_length=21)
    description = models.TextField()
    level = models.CharField(max_length=21, null=True, blank=True)
    image = models.TextField()
    in_game_image = models.TextField(null=True, blank=True)
