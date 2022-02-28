from django.shortcuts import render
from realtor.models import Realtor
from realtor.serializer import RealtorSerializer
from rest_framework import generics


# Create your views here.

class RealtorList(generics.ListAPIView):
    queryset = Realtor.objects.all()
    serializer_class = RealtorSerializer


def list_realtor(request):
    realist = Realtor.objects.all()
    context = {
        'realist': realist
    }
    return render(request, 'Listing/realtor.html', context)
