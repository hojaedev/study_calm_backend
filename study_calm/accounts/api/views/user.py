from django.shortcuts import render

from accounts.models import User
from ..serializers import UserListSerializer, UserDetailSerializer
from rest_framework import generics

class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserDetailSerializer

class UserDetail(generics.RetrieveDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserDetailSerializer


