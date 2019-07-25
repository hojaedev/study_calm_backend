from rest_framework import serializers
from listings.models import Seat


class SeatListSerializer(serializers.ModelSerializer):

    # author = UserSerializer()
    # comments = CommentSerializer(many=True)

    class Meta:
        model = Seat
        fields = [
            'id',
            'nth_seat',
            'extendable',
            'in_use',
            'in_use_until',
        ]

class SeatDetailSerializer(serializers.ModelSerializer):
    # # listing = ListingDetailSerializer(source='listing', read_only=True)
    # user = UserDetialSerializer(read_only=True)
    # # details = ProductDetailSerializer(read_only=True)
    #
    # # Seats will always be in default to prevent overbooking
    # in_use = serializers.BooleanField()
    # in_use_until = serializers.DateTimeField()

    class Meta:
        model = Seat
        fields = [
            'id',
            'user',
            'nth_seat',
            'extendable',
            'in_use',
            'in_use_until',
            # 'details',
        ]
        read_only_fields = ('id',)
        # depth=1
