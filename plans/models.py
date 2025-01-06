from django.db import models

# Create your models here.

class Exercise(models.Model):
    name = models.CharField(max_length=254, null=True, blank=True, default="")
    video = models.FileField(blank=True, null=True)
    description = models.TextField(null=True, blank=True, default="")
    abs_name = models.CharField(max_length=254, null=True, blank=True, default="")
    abs_video = models.FileField(blank=True, null=True)
    abs_description = models.TextField(null=True, blank=True, default="")
    sets = models.IntegerField(null=True, blank=True, default=1)
    reps = models.IntegerField(null=True, blank=True, default=1)
  
    def __str__(self):
        return f"{self.name} | {self.abs_name}"

class MealPlan(models.Model):
    name = models.CharField(max_length=254)
    slug = models.SlugField(max_length=200, unique=True, default="", null=False)
    image = models.ImageField(blank=True, null=True)
    description = models.TextField()
    calories = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
