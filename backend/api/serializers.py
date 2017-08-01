from rest_framework import serializers
from api.models import Country, Pinned, User


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ('id', 'code', 'name')


class PinnedSerializer(serializers.ModelSerializer):

    def to_representation(self, value):
        pin = value.pinned_set.first()
        return { "country_id": pin.country_id, "type": pin.type }

    class Meta:
        model = Pinned


class UserSerializer(serializers.ModelSerializer):
    pins = PinnedSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'pins')
