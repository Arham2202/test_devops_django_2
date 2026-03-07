from django.urls import path
from students import views

urlpatterns = [
    path('', views.registration, name='registration'),
    path('students/', views.studentlist, name='studentlist'),
] 