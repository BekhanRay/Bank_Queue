from django.shortcuts import render

from .models import Users
from .serializer import UsersSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics


class UserView(generics.ListCreateAPIView):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer


class UsersView(APIView):

    def get(self, request, format=None):
        """
        Return a list of all users.
        """
        usernames = [user.username for user in Users.objects.all()]
        return Response(usernames)

    def post(self, request, format=None):
        serializer = UsersSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
