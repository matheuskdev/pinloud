from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from accounts.models import User

from ..models import Pin


class PinViewTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(
            email="test@example.com", password="testpass"
        )
        self.client.force_authenticate(user=self.user)

    def test_create_pin(self):
        data = {
            "title": "Test Pin",
            "description": "This is a test pin.",
            "image": "path/to/image.jpg",
        }
        response = self.client.post(reverse("pin-list"), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Pin.objects.count(), 1)
        self.assertEqual(Pin.objects.get().title, "Test Pin")

    def test_list_pins(self):
        Pin.objects.create(
            title="Pin  1", description="Description  1", user=self.user
        )
        Pin.objects.create(
            title="Pin  2", description="Description  2", user=self.user
        )
        response = self.client.get(reverse("pin-list"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
        self.assertEqual(response.data[0]["title"], "Pin  1")
        self.assertEqual(response.data[1]["title"], "Pin  2")

    def test_update_pin(self):
        pin = Pin.objects.create(
            title="Old Title", description="Old Description", user=self.user
        )
        new_data = {
            "title": "New Title",
            "description": "New Description",
        }
        response = self.client.put(
            reverse("pin-detail", args=[pin.id]), new_data
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        pin.refresh_from_db()
        self.assertEqual(pin.title, "New Title")
        self.assertEqual(pin.description, "New Description")

    def test_delete_pin(self):
        pin = Pin.objects.create(
            title="To Delete", description="Delete Me", user=self.user
        )
        response = self.client.delete(reverse("pin-detail", args=[pin.id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Pin.objects.count(), 0)
