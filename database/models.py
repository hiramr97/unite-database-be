from django.db import models

# Create your models here.
class Pokemon(models.Model):
    name = models.CharField(max_length=21)
    difficulty = models.CharField(max_length=21)
    role = models.CharField(max_length=21)
    image = models.TextField()

    def __str__(self):
        return self.name