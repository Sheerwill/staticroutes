from django.test import TestCase
from Restaurant.models import Menu
from Restaurant.serializers import MenuSerializer
from django.urls import reverse
from rest_framework.test import APIClient

class MenuViewTest(TestCase):
    def setUp(self):

        self.item1 = Menu.objects.create(ID=123456, Title="IceCream", Price=80, Inventory=100)
        self.item2 = Menu.objects.create(ID=123457, Title="Lasagna", Price=90, Inventory=110)
        self.item3 = Menu.objects.create(ID=123458, Title="Hummus", Price=100, Inventory=120)

    def test_getall(self):
        self.client = APIClient()  # Initialize the test client
        self.url = reverse("menu-list")
        response = self.client.get(self.url)

        serialized_data = MenuSerializer([self.item1, self.item2, self.item3], many=True).data 
        self.assertEqual(response.data, serialized_data)
        
        
