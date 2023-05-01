from django.db import models

# Create your models here.
class Pokemon(models.Model):
    name = models.CharField(max_length=21)
    difficulty = models.CharField(max_length=21)
    role = models.CharField(max_length=21)
    image = models.TextField()

    def __str__(self):
        return self.name
    
class Evolution(models.Model):
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE, related_name='evolution')
    name = models.CharField(max_length=21)
    level = models.CharField(max_length=7)
    image = models.TextField()

    def __str__(self):
        return self.name

class Builds(models.Model):
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE, related_name='builds')
    name = models.CharField(max_length=21)
    lane = models.CharField(max_length=7)

    def __str__(self):
        return self.name
    
class HeldItems(models.Model):
    build = models.ForeignKey(Builds, on_delete=models.CASCADE, related_name='held_items')
    name = models.CharField(max_length=21)
    image = models.TextField()

    def __str__(self):
        return self.name
    
class BattleItems(models.Model):
    build = models.ForeignKey(Builds, on_delete=models.CASCADE, related_name='battle_items')
    name = models.CharField(max_length=21)
    image = models.TextField()
    optional_name = models.CharField(max_length=21)
    optional_image = models.TextField()

    def __str__(self):
        return self.name
    
