from django.db import models

# Create your models here.

class Exercise(models.Model):
    name = models.CharField(max_length=254, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    video = models.FileField(blank=True, null=True)
    description = models.TextField(null=True, blank=True)
    # glutes_name = models.CharField(max_length=254, null=True, blank=True)
    # abs_name = models.CharField(max_length=254)
    # glutes_image = models.ImageField(null=True, blank=True)
    # abs_image = models.ImageField(null=True, blank=True)
    # glutes_video = models.FileField(blank=True, null=True)
    # abs_video = models.FileField(blank=True, null=True)
    # glutes_description = models.TextField(null=True, blank=True)
    # abs_description = models.TextField(null=True, blank=True)
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

  

