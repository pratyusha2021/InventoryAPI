from django.shortcuts import render
from .serializers import WatchlistSerializer, StreamSerializer
from .models import Watchlist, StreamPlatform
from rest_framework import generics

# Create your views here.
class WatchView(generics.ListCreateAPIView):
    queryset = Watchlist.objects.all()
    serializer_class = WatchlistSerializer

class WatchDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Watchlist.objects.all()
    serializer_class = WatchlistSerializer

class StreamView(generics.ListCreateAPIView):
    queryset = StreamPlatform.objects.all()
    serializer_class = StreamSerializer

class StreamDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = StreamPlatform.objects.all()
    serializer_class = StreamSerializer
