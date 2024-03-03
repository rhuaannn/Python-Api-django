from django.db import models


NATIONALITY_CHOICE = (
    ('BRASIL', 'BRA'),
    ('ESTADOS-UNIDOS', 'USA'),
    ('ARGENTINA', 'ARG'),
)


class Actors(models.Model):
    name = models.CharField(max_length=70)
    birthday = models.DateField(null=True, blank=True)
    nationality = models.CharField(max_length=70, choices=NATIONALITY_CHOICE, blank=True, null=True)

    def __str__(self):
        return self.name
