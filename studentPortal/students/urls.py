from django.urls import path
from students.views import home
from students import views

urlpatterns = [
    path('', home, name='home'),
    path('students/', views.studentlist, name='studentlist'),
] 