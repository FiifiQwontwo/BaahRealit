from django.urls import path
from .views import ListingList, listview

urlpatterns = [
    path('listapi/', ListingList.as_view()),
    path('list_/', listview, name='list_listing'),

]
