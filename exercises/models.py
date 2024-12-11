from django.db import models

# Create your models here.

class Exercise(models.Model):
    name = models.CharField(max_length=254)
    image = models.ImageField(null=True, blank=True)
    video = models.FileField(blank=True, null=True)
    description = models.TextField()
    sets = models.IntegerField()
    reps = models.IntegerField()
    warm_up = models.TextField()
  
    def __str__(self):
        return self.name


