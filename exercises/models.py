from django.db import models

# Create your models here.

class Exercise(models.Model):
    name= models.CharField(max_length=254)
    image = models.ImageField(null=True, blank=True)
    video = models.FileField(blank=True, null=True)
    description = models.TextField()
    sets1 = models.IntegerField(null=True, blank=True)
    reps1 = models.IntegerField(null=True, blank=True)
    sets2 = models.IntegerField(null=True, blank=True)
    reps2 = models.IntegerField(null=True, blank=True)
    sets3 = models.IntegerField(null=True, blank=True)
    reps3 = models.IntegerField(null=True, blank=True)
    sets4 = models.IntegerField(null=True, blank=True)
    reps4 = models.IntegerField(null=True, blank=True)
  
    def __str__(self):
        return self.name

class Abs_exercise(models.Model):
    name= models.CharField(max_length=254)
    image = models.ImageField(null=True, blank=True)
    video = models.FileField(blank=True, null=True)
    description = models.TextField()
    sets1 = models.IntegerField(null=True, blank=True)
    reps1 = models.IntegerField(null=True, blank=True)
    sets2 = models.IntegerField(null=True, blank=True)
    reps2 = models.IntegerField(null=True, blank=True)
    sets3 = models.IntegerField(null=True, blank=True)
    reps3 = models.IntegerField(null=True, blank=True)
    sets4 = models.IntegerField(null=True, blank=True)
    reps4 = models.IntegerField(null=True, blank=True)
     
    def __str__(self):
        return self.name
  

