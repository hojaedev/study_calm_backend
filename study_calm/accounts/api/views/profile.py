from accounts.api.serializers import CustomerProfileSerializer, SupplierProfileSerializer
from rest_framework import generics
from rest_framework import permissions
from rest_framework import status
from rest_framework.views import Response


class CustomerView(generics.RetrieveAPIView):
    serializer_class = CustomerProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, **kwargs):
        return Response(status=status.HTTP_200_OK)

class SupplierView(generics.RetrieveAPIView):
    serializer_class = SupplierProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, **kwargs):
        return Response(status=status.HTTP_200_OK)