from django.db import models

from django.shortcuts import render
from rest_framework import generics, serializers
from .models import SuperPlayer
from .serializers import PlayerSerializer 
from .permissions import IsAuthorOrReadOnly
# Create your views here.
class PlayersListView(generics.ListCreateAPIView):
    serializer_class = PlayerSerializer
    queryset = SuperPlayer.objects.all()
class PlayersDetailsView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PlayerSerializer
    queryset = SuperPlayer.objects.all()
    permission_classes  = (IsAuthorOrReadOnly,)