from Movies_app.models import Watchlist, StreamPlatform
from rest_framework import serializers

class WatchlistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Watchlist
        fields = "__all__"

class StreamSerializer(serializers.ModelSerializer):
    watchlists = WatchlistSerializer(many = True, read_only = True)

    class Meta:
        model = StreamPlatform
        fields = "__all__"

