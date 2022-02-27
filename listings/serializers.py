from rest_framework import serializers
from listings.models import Listing


class ListingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Listing
        fields = ('realtor', 'title', 'description',
                  'address', 'region', 'city', 'currency',
                                               'price', 'price_per_month', 'bedrooms',
                  'square_size', 'lot_size', 'garage', 'swimming_pool', 'newly_built',
                  'boys_quarters', 'furnished', 'furnished_state', 'main_image', 'main_image6', 'main_image5',
                  'main_image4', 'main_image3', 'image2', 'property_video', 'floor_plan', 'first_floor',
                  'published', 'created_at',
                  )
