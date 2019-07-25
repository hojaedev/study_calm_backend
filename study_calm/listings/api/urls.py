from django.contrib import admin
from django.urls import path, re_path
from django.conf.urls import url, include

from .views import (
    ListingDeleteAPIView,
    ListingDetailAPIView,
    ListingListAPIView,
    ListingUpdateAPIView,
    SeatListView,
    SeatDetailView,
    SeatReturnView,
    SeatSelectView,
)

listing_urlpatterns = [

    # LISTING
    path('', ListingListAPIView.as_view(), name='list'),
    path('listing/<int:id>/', ListingDetailAPIView.as_view(), name='detail'),
    path('listing/<int:id>/edit/', ListingUpdateAPIView.as_view(), name='update'),
    path('listing/<int:id>/delete/', ListingDeleteAPIView.as_view(), name='delete'),

    # DETAIL
    path('seat/', SeatListView.as_view()),
    path('seat/<uuid:id>/', SeatDetailView.as_view()),
    path('seat/<uuid:id>/select/', SeatSelectView.as_view()),
    path('seat/<uuid:id>/return/', SeatReturnView.as_view()),
]

# url(r'^/seat/(?P<pk>\w+)/$', ....)