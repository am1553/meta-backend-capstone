from django import test
from ..models import MenuItem, Booking


class MenuItemTest(test.TestCase):

    def test_getall(self):
        item = MenuItem.objects.create(title="IceCream", price=80, inventory=100)
        self.assertEqual(str(item), "IceCream : 80")