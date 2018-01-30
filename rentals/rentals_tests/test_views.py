from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from rentals.models import Rental, Comment


class RentalIndexViewTests(TestCase):
    def test_no_rental(self):
        """
        If no rentals exist, an appropriate message is displayed
        """
        response = self.client.get(reverse('rentals:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'No rentals Avilable')
        self.assertQuerysetEqual(response.context['rentals_list'], [])
