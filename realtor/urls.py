from django.urls import path
from .views import RealtorList

urlpatterns = [
    path('realtorsapi/', RealtorList.as_view()),


]