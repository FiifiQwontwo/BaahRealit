from django.urls import path
from .views import succesview, contactview

app_name = 'contact'

urlpatterns = [
    path('send_message/', contactview, name='contact'),
    path('succes/', succesview, name='success_mail'),
]
