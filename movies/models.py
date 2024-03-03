from django.db import models
from actors.models import Actors
from genres.models import Genre


class Movies(models.Model):
    genre = models.ForeignKey(Genre, on_delete=models.PROTECT, related_name='movies')
    title = models.CharField(max_length=500)
    release_date = models.DateField(null=True, blank=True)
    actors = models.ManyToManyField(Actors, related_name='movies')
    resume = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title
