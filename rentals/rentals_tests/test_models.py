from django.test import TestCase
from django.utils import timezone
from django.urls import reverse

from rentals.models import Rental, Comment

# Create your tests here.

class RentalModelTestCase(TestCase):

    @classmethod
    def setUpTestData(cls):
        Rental.objects.create(title='A new title',
                            description='A super cool description',
                            rent=10,
                            location='Pokhara, Nepal',
                        )

    def setUp(self):
        pass

    def test_rental_fields(self):
        obj = Rental.objects.get(title="A new title")
        self.assertEqual(obj.title, 'A new title')

    def test_title_name_label(self):
        rental = Rental.objects.get(id=1)
        field_label = rental._meta.get_field('title').verbose_name
        self.assertEquals(field_label, 'title')
