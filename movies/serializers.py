from django.db.models import Avg
from rest_framework import serializers
from genres.serializers import GenreSerializer
from movies.models import Movies
from actors.serializers import ActorGetNameSerializer


class MoviesSerializer(serializers.ModelSerializer):

    rate = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Movies
        fields = '__all__'

    def get_rate(self, obj):
        rate = obj.reviews.aggregate(Avg('stars'))['stars__avg']

        if rate:
            return round(rate, 1)
        return 'Avaliçãoes insuficiente '

    def validate_release_date(self, value):
        if value.year <= 1900:
            raise serializers.ValidationError(
                'Data inferior a 1990 não é permitido.')
        return value

    def validate_resume(self, value):
        if len(value) > 200:
            raise serializers.ValidationError(
                'Resume não deve ser maior que 200 caracteres.')
        return value


class MoviesGetSerializer(serializers.ModelSerializer):
    actors = ActorGetNameSerializer(many=True)
    genre = GenreSerializer()
    rate = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Movies
        fields = ['id', 'title', 'genre',
                  'actors', 'release_date', 'resume', 'rate', ]

    def get_rate(self, obj):
        rate = obj.reviews.aggregate(Avg('stars'))['stars__avg']

        if rate:
            return round(rate, 1)
        return 'Avaliações insuficientes para calcular uma média'
