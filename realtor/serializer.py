from rest_framework import serializers
from realtor.models import Realtor
from listings.serializers import ListingSerializer


class RealtorSerializer(serializers.ModelSerializer):
    listings = ListingSerializer(many=True, read_only=True)

    class Meta:
        model = Realtor
        fields = ('last_name', 'first_name', 'name_of_agency', 'photo', 'mvp', 'listings')