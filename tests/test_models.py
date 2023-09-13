from django.test import TestCase
from Restaurant.models import Menu

class TestMenu(TestCase):
    def test_menu(self):
        item = Menu.objects.create(ID = 123456, Title="IceCream", Price=80, Inventory=100)
        self.assertEqual(str(item), "IceCream : 80")