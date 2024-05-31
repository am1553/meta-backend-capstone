from django.test import TestCase
from ..models import MenuItem
from django.urls import reverse
from ..serializers import MenuItemSerializer

class MenuItemViewTest(TestCase):
    
    def setup():
        menuitem = MenuItem.objects.create(title="IceCream", price=80, inventory=100).save()
    
    def test_list(self):
        response = self.client.get(reverse('menu'))
        serializer = MenuItemSerializer(MenuItem.objects.all(), many=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, serializer.data)