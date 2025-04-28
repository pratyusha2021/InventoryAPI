
from django.urls import path
from .views import WatchView, WatchDetail, StreamView, StreamDetail

urlpatterns = [
    path('watch-list/', WatchView.as_view(), name = "list-view"),
    path('watch-detail/<int:pk>/', WatchDetail.as_view(), name = "detail-view"),
    path('stream-list/', StreamView.as_view(), name = "stream-list"),
    path('stream-watch/<int:pk>/', StreamDetail.as_view(), name = "stream-detail")
]