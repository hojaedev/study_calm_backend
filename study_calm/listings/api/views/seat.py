from listings.models import Seat
from django.shortcuts import get_list_or_404, get_object_or_404
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from django.http import Http404
from rest_framework import status
from ..serializers import SeatDetailSerializer, SeatListSerializer
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer

class SeatListView(GenericAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [AllowAny]
    serializer_class = SeatListSerializer
    queryset = Seat.objects.all()
    filter_item = ['listing__id', 'in_use']

    def get_list(self, **kwargs):
        queryset = self.get_queryset()
        filter = {}
        for field in self.request.GET:
            if field in self.filter_item:
                filter[field] = self.request.GET[field]
        obj = get_list_or_404(queryset, **filter)
        return obj

    def get(self, request, *args, **kwargs):
        print(request.GET)
        if request.GET.get('listing__id', None):
            obj = self.get_list()
            serializer = self.serializer_class(obj, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_404_NOT_FOUND)

    '''
    SUPPLIER
    Register a List of Seats
    '''

class SeatDetailView(GenericAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [AllowAny]
    pk_url_kwarg = 'id'
    serializer_class = SeatDetailSerializer

    def get_object(self, id):
        queryset = Seat.objects.get(id=id)
        obj = get_object_or_404(queryset)
        return obj

    def get(self, request, *args, **kwargs):
        seat = self.get_object(kwargs['id'])
        if seat:
            serializer = self.serializer_class(seat, many=False)
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def post(self, request, *args, **kwargs):
        print(request)
        return Response(stauts=status.HTTP_200_OK)


class SeatReturnView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [AllowAny]
    pk_url_kwarg = 'id'
    serializer_class = SeatDetailSerializer
    allowed_method = ['GET','POST']

    def get_object(self, pk):
        try:
            return Seat.objects.all().filter(id=pk).first()
        except Seat.DoesNotExist:
            raise Http404

    def post(self, request, *args, **kwargs):
        print(request)
        seat = self.get_object(kwargs['id'])
        if seat.user == request.user:
            return Response(status=status.HTTP_200_OK)

class SeatSelectView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [AllowAny]
    pk_url_kwarg = 'id'
    serializer_class = SeatDetailSerializer
    allowed_method = ['GET']

    def post(self, request, *args, **kwargs):
        print(request.user)
        return Response(status=status.HTTP_200_OK)



