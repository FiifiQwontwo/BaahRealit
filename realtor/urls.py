from django.urls import path
from .views import RealtorList, list_realtor

urlpatterns = [
    path('realtorsapi/', RealtorList.as_view()),
    path('real/', list_realtor, name='List_realtor'),

]
