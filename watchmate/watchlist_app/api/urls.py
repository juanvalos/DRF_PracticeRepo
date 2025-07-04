from django.urls import path, include
from watchlist_app.api.views import WatchListAV, WatchDetailAV, StreamPlatformAV, StreamPlatformDetailAV

urlpatterns = [
    path('stream/', StreamPlatformAV.as_view(), name='stream-list'),
    path('stream/<int:pk>', StreamPlatformDetailAV.as_view(), name='stream-detail'),
    path('watch/', WatchListAV.as_view(), name='watchlist'),
    path('watch/<int:pk>', WatchDetailAV.as_view(), name='watch-detail'),
]