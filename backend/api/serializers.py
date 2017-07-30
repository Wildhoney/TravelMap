from rest_framework import serializers
from api.models import Country, Pinned, User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'countries')


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ('id', 'code', 'name')


class PinnedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pinned
        fields = ('country_id', 'user_id', 'type')
