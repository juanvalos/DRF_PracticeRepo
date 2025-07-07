from django.urls import path, include
from watchlist_app.api.views import WatchListAV, WatchDetailAV, StreamPlatformAV, StreamPlatformDetailAV, ReviewList, ReviewDetail, ReviewCreate

urlpatterns = [
    path('stream/', StreamPlatformAV.as_view(), name='stream-list'),
    path('stream/<int:pk>', StreamPlatformDetailAV.as_view(), name='stream-detail'),
    
    path('list/', WatchListAV.as_view(), name='watchlist'),
    path('<int:pk>', WatchDetailAV.as_view(), name='watch-detail'),
    
    path('stream/<int:pk>/review-create', ReviewCreate.as_view(), name = 'review-create'),
    path('stream/<int:pk>/review', ReviewList.as_view(), name = 'review-list'),
    path('review/<int:pk>', ReviewDetail.as_view(), name = 'review-detail'),
]