from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics
from .models import MenuItem
from .serializers import MenuItemSerializer


def index(request):
    return render(request, 'index.html', {})


class MenuItemView(generics.ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer


class SingleMenuItem(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    serializer_class = MenuItemSerializer
    def get_queryset(self):
        menu = MenuItem.objects.all().filter(id=self.kwargs['pk'])
        return menu

