from django.contrib.auth.models import User
from django.http import HttpResponse
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.compat import authenticate
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.parsers import JSONParser
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from users.serializers import UserSerializer

"""
Example of requests, make sure you use correct token

curl -X GET http://127.0.0.1:8000/users/users/ -H 'Authorization: Token 944d95490a351ee5aaa7de8b967c50454047c161'

curl -X GET http://127.0.0.1:8000/users/user/me/ -H 'Authorization: Token 57cac39bdbce2afb13b4124d7aaa99d3072d0d76'
"""


class AllUsers(ListAPIView):
    """
        Send list of all user registered in app after authorization by token
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserLogin(APIView):
    """
        Make token available for user if his credentials (email, password) are correct
    """

    permission_classes = [AllowAny]

    def post(self, request, format=None):
        data = JSONParser().parse(request)
        user = User.objects.filter(email=data['email']).first()
        if user is not None:
            user = authenticate(username=user.username, password=data['password'])
            if user is not None:
                if user.is_active:
                    token = Token.objects.get_or_create(user=user)
                    return Response({'token': token[0].key})
            else:
                return HttpResponse(status=401)
        else:
            return HttpResponse(status=401)


class CreateUser(APIView):
    """
        Register new user, required: username, email, password
    """
    permission_classes = [AllowAny]

    def put(self, request,format=None):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token = Token.objects.get_or_create(user=user)
            return Response({'token': token[0].key}, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserDetail(APIView):
    """
        Endpoint authorization by token, response contain user details
    """

    def get(self, request, format=None):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)
