# from django.db import models

# # Create your models here.

# class Exercise(models.Model):
#     name = models.CharField(max_length=254, null=False, blank=False, default="")
#     video = models.FileField(blank=True, null=True)
#     description = models.TextField(null=False, blank=False, default="")
#     abs_name = models.CharField(max_length=254, null=False, blank=False, default="")
#     abs_video = models.FileField(blank=True, null=True)
#     abs_description = models.TextField(null=False, blank=False, default="")
#     sets = models.IntegerField(null=False, blank=False, default=1)
#     reps = models.IntegerField(null=False, blank=False, default=1)
  
#     def __str__(self):
#         return f"{self.name} | {self.abs_name}"

# class MealPlan(models.Model):
#     name = models.CharField(max_length=254)
#     slug = models.SlugField(max_length=200, unique=True, default="", null=False)
#     description = models.TextField()
#     calories_per_day = models.IntegerField()
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return self.name

  

