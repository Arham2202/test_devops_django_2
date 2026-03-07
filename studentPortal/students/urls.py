from django.urls import path
from students.views import home
from students import views

urlpatterns = [
    path('', home, name='registration'),
    path('students/', views.studentlist, name='studentlist'),
] 