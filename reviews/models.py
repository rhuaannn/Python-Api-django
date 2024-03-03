from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from movies.models import Movies


class Review(models.Model):
    movie = models.ForeignKey(Movies, on_delete=models.PROTECT, related_name='reviews')
    stars = models.IntegerField(validators=[
        MinValueValidator(0, 'Minimo de estrela é 0'),
        MaxValueValidator(5, 'O máximo de estrela é 5')
    ])
    comment = models.TextField(null=True, blank=True)    

    def __str__(self):
        return str(self.movie)
