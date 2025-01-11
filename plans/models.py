from django.db import models

# Create your models here.

class GlutesExercise(models.Model):
    name = models.CharField(max_length=254, null=False, blank=False, default="")
    video = models.FileField(null=True, blank=True)
    description = models.TextField(null=False, blank=False, default="")
    sets = models.IntegerField(null=False, blank=False, default=1)
    reps = models.IntegerField(null=False, blank=False, default=1)
  
    def __str__(self):
        return f"{self.name}"

class AbsExercise(models.Model):
    name = models.CharField(max_length=254, null=False, blank=False, default="")
    video = models.FileField(null=True, blank=True)
    description = models.TextField(null=False, blank=False, default="")
    sets = models.IntegerField(null=False, blank=False, default=1)
    reps = models.IntegerField(null=False, blank=False, default=1)

    def __str__(self):
        return f"{self.name}"

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

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(MealPlan, self).save(*args, **kwargs)
