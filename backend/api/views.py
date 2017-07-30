from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from django.contrib.auth.models import User
from api.models import Country
from api.serializers import CountrySerializer, UserSerializer


class CountryList(APIView):

    def get(self, request, format=None):
        countries = Country.objects.all()
        serializer = CountrySerializer(countries, many=True)
        return Response(serializer.data)


class UserProfile(APIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def get(self, request, username, format=None):
        user = User.objects.get(username=username)
        serializer = UserSerializer(user)
        return Response(serializer.data)
