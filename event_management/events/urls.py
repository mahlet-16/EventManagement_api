from django.urls import path
from .views import CustomTokenObtainPairView

from .views import (
    EventListCreateAPIView, EventRetrieveUpdateDeleteAPIView,
    RegisterForEventAPIView, CategoryListAPIView, LocationListAPIView,
    UserRegistrationAPIView, 
)

urlpatterns = [
    path('events/', EventListCreateAPIView.as_view(), name='event-list-create'),
    path('events/<int:pk>/', EventRetrieveUpdateDeleteAPIView.as_view(), name='event-detail'),
    path('register/', RegisterForEventAPIView.as_view(), name='register-event'),
    path('categories/', CategoryListAPIView.as_view(), name='category-list'),
    path('locations/', LocationListAPIView.as_view(), name='location-list'),
    
    # User registration and login endpoints
    path('user/register/', UserRegistrationAPIView.as_view(), name='user-register'),
    path('user/login/', CustomTokenObtainPairView.as_view(), name='login'),
]
