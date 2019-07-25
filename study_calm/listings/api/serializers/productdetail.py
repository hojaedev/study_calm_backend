from rest_framework import serializers
from listings.models import ProductDetail

class ProductDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductDetail
        fields = [
            'id',
            'type',
            'price',
            'long_name_kr',
            'long_name_en',
            'detail',
        ]
