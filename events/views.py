from rest_framework import generics, permissions, status
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import Event, Registration, Category, Location
from .serializers import EventSerializer, RegistrationSerializer, CategorySerializer, LocationSerializer, UserRegistrationSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User
import logging
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
# Custom Login View to only return access token
class CustomTokenObtainPairView(TokenObtainPairView):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        # We only return the access token, removing the refresh token from the response
        return Response({'access': response.data['access']})


# User Registration View
class UserRegistrationAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            'message': 'User created successfully'
        })

# CRUD for Events
class EventListCreateAPIView(generics.ListCreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['title', 'location__name', 'category__name']
    authentication_classes = [JWTAuthentication]

    def perform_create(self, serializer):
        try:
            serializer.save(organizer=self.request.user)
        except Exception as e:
            logging.error(f"Error while creating event: {e}")
            raise

class EventRetrieveUpdateDeleteAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def perform_update(self, serializer):
        event = self.get_object()
        if event.organizer != self.request.user:
            return Response({"error": "You can only edit your own events."}, status=status.HTTP_403_FORBIDDEN)
        serializer.save()

# Event Registration
class RegisterForEventAPIView(generics.CreateAPIView):
    queryset = Registration.objects.all()
    serializer_class = RegistrationSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [JWTAuthentication]

# List all Categories
class CategoryListAPIView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.AllowAny]

# List all Locations
class LocationListAPIView(generics.ListAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    permission_classes = [permissions.AllowAny]
