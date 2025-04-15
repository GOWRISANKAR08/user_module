
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserProfileViewSet

urlpatterns = [
    path('', views.UserProfileViewSet, name='user-home'),
]