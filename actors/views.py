from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from app.permission import GlobalDefaultPermission
from actors.models import Actors
from actors.serializers import ActorSerializer


class ActorCreateListview(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission)
    queryset = Actors.objects.all()
    serializer_class = ActorSerializer


class ActorRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission)
    queryset = Actors.objects.all()
    serializer_class = ActorSerializer
