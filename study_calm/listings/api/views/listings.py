from rest_framework.generics import (
    CreateAPIView,
    DestroyAPIView,
    ListAPIView,
    RetrieveAPIView,
    UpdateAPIView,
)
from listings.models import Listing
from listings.api.serializers import (
    ListingListSerializer,
    ListingDetailSerializer,
    ListingCreateSerializer
)

class ListingCreateAPIView(CreateAPIView):
    queryset = Listing.objects.all()
    serializer_class = ListingCreateSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class ListingDetailAPIView(RetrieveAPIView):
    queryset = Listing.objects.all()
    serializer_class = ListingDetailSerializer

    # lookup_field = 'slug'
    # lookup_url_kwarg = 'abc'
    # <abc>

class ListingListAPIView(ListAPIView):
    queryset = Listing.objects.all()
    serializer_class = ListingListSerializer


class ListingUpdateAPIView(UpdateAPIView):
    queryset = Listing.objects.all()
    serializer_class = ListingDetailSerializer

class ListingDeleteAPIView(DestroyAPIView):
    queryset = Listing.objects.all()
    serializer_class = ListingDetailSerializer