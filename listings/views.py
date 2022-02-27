from django.shortcuts import render
from rest_framework import generics
from .models import Listing
from .serializers import ListingSerializer


# Create your views here.

class ListingList(generics.ListAPIView):
    queryset = Listing.objects.order_by('-created_at')
    serializer_class = ListingSerializer


def listview(request):
    ase = Listing.objects.order_by('-created_at')
    context = {
        'ase': ase
    }
    return render(request, 'listing/listListing.html', context)
