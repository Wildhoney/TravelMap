from rest_framework import serializers
from django.contrib.auth.models import User
from api.models import Country, Pinned

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username')


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ('id', 'code', 'name')


class PinnedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pinned
        fields = ('country_id', 'user_id', 'type')
