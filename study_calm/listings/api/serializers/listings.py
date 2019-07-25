from rest_framework import serializers

from listings.models import Listing

class ListingListSerializer(serializers.ListSerializer):
    class Meta:
        model = Listing
        fields = [
            'id',
            'owner',
            'name',
            'address',
            'geo_lat',
            'geo_lng',
        ]

class ListingDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Listing
        fields = [
            'id',
            'owner',
            'name',
            'address',
            'geo_lat',
            'geo_lng',
        ]

class ListingCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Listing