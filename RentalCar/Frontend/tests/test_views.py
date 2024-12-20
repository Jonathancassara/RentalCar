from django.test import TestCase
from django.urls import reverse
from Frontend.models import Driver

class DriverViewTests(TestCase):
    def setUp(self):
        self.driver = Driver.objects.create(
            name="Jane",
            surname="Doe",
            email="jane@example.com",
            phone_number="0987654321"
        )

    def test_driver_list_view(self):
        response = self.client.get(reverse('driver_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'Frontend/driver_list.html')
        self.assertContains(response, "Jane")

    def test_create_driver_view(self):
        response = self.client.post(reverse('create_driver'), {
            'name': 'New',
            'surname': 'Driver',
            'email': 'newdriver@example.com',
            'phone_number': '5555555555'
        })
        self.assertEqual(response.status_code, 302)  # Redirect after creation
        self.assertTrue(Driver.objects.filter(name="New").exists())

    def test_update_driver_view(self):
        response = self.client.post(reverse('update_driver', args=[self.driver.id]), {
            'name': 'Updated',
            'surname': 'Driver',
            'email': 'updated@example.com',
            'phone_number': '5555555555'
        })
        self.assertEqual(response.status_code, 302)
        self.driver.refresh_from_db()
        self.assertEqual(self.driver.name, "Updated")
