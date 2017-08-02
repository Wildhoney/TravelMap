from rest_framework import serializers
from api.models import Country, Pinned, User


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ('id', 'code', 'name')


class PinnedSerializer(serializers.ModelSerializer):
    country_id = serializers.ReadOnlyField(source='country.id')
    class Meta:
        model = Pinned
        fields = ('type', 'country_id')


class UserSerializer(serializers.ModelSerializer):
    pinned_set = PinnedSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'pinned_set')
