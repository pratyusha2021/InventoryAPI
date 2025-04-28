from django.db import models

# Create your models here.

class StreamPlatform(models.Model):
    id = models.AutoField(primary_key= True)
    name = models.CharField(max_length=20)
    about = models.CharField(max_length=30)
    website = models.URLField(max_length=100)

    def __str__(self):
        return self.name

class Watchlist(models.Model):
    id = models.AutoField(primary_key= True)
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=40)
    active = models.BooleanField(default=True)
    #created = models.DateTimeField(auto_now_add=True)
    platform = models.ForeignKey(StreamPlatform, on_delete=models.CASCADE, related_name="watchlists")

    def __str__(self):
        return self.title

