from django.db import models
from django.contrib.auth.models import User

class Recipe(models.Model):
    Meals = [
        ('Breakfast', 'Breakfast'),
        ('Lunch', 'Lunch'),
        ('Super', 'Super'),
    ]

    title = models.CharField(max_length=200)
    ingredients = models.TextField()
    instructions = models.TextField()
    category = models.CharField(max_length=50, choices=Meals)
    image = models.ImageField(upload_to='recipe_images/', blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
