from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics, viewsets, permissions
from .models import MenuItem, Booking
from .serializers import MenuItemSerializer, BookingSerializer


def index(request):
    return render(request, 'index.html', {})


class MenuItemView(generics.ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    permission_classes = [permissions.AllowAny]


class SingleMenuItem(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    serializer_class = MenuItemSerializer
    permission_classes = [permissions.IsAuthenticated]
    def get_queryset(self):
        menu = MenuItem.objects.all().filter(id=self.kwargs['pk'])
        return menu


class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [permissions.IsAuthenticated]
    