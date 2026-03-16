from django.urls import path
from . import views

urlpatterns = [
    path('', views.user_login, name="login"),
    path('register/', views.register, name="register"),
    path('logout/', views.user_logout, name="logout"),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('add_expense/', views.add_expense, name="add_expense"),
    path('add_income/', views.add_income, name="add_income"),
    path('delete_expense/<int:id>/', views.delete_expense, name="delete_expense"),
]