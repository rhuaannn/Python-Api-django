from rest_framework import generics, views, response, status
from django.db.models import Count, Avg
from rest_framework.permissions import IsAuthenticated
from app.permission import GlobalDefaultPermission
from movies.models import Movies
from movies.serializers import MoviesGetSerializer, MoviesSerializer
from reviews.models import Review


class MovieCreateListView(generics.ListCreateAPIView):

    permission_classes = (IsAuthenticated, GlobalDefaultPermission)
    queryset = Movies.objects.all()
    serializer_class = MoviesSerializer

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return MoviesGetSerializer
        return MoviesSerializer


class MovieRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission)
    queryset = Movies.objects.all()
 

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return MoviesGetSerializer
        return MoviesSerializer



class MovieStatsView(views.APIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission)
    queryset = Movies.objects.all()

    def get(self, request):

        total_movies = self.queryset.count()
        movies_by_genres = self.queryset.values(
            'genre__name').annotate(count=Count('id'))
        total_reviews = Review.objects.count()
        avarege_stars = Review.objects.aggregate(
            avg_stars=Avg('stars'))['avg_stars']

        return response.Response(
            data={
                'total_movies': total_movies,
                'movies_by_genres': movies_by_genres,
                'total_reviews': total_reviews,
                'avarege_stars': round(avarege_stars, 1) if avarege_stars else 0,
            },
            status=status.HTTP_200_OK,
        )
