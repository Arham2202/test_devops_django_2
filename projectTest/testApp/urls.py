from django.urls import path
from testApp.views import home

urlpatterns = [
    path('', home, name='home'),
]