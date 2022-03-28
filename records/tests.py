from django.test import TestCase

# Create your tests here.

from .models import Record


class RecordTestCase(TestCase):

    def setUp(self):
        self.number_of_records = 10
        for i in range(0, self.number_of_records):
            Record.objects.create(
                title='Hello World',
                quantity=100,
                distance=50.61,
                date='2012-06-01'
            )

    def test_queryset_exists(self):
        qs = Record.objects.all()
        self.assertTrue(qs.exists())

    def test_record_search_title(self):
        qs = Record.objects.filter_title(search_query='World', chosen_option='contains')
        self.assertEqual(qs.count(), self.number_of_records)
        qs = Record.objects.filter_title(search_query='Hello World', chosen_option='equals to')
        self.assertEqual(qs.count(), self.number_of_records)

    def test_record_search_quantity(self):
        qs = Record.objects.filter_quantity(search_query='1', chosen_option='contains')
        self.assertEqual(qs.count(), self.number_of_records)
        qs = Record.objects.filter_quantity(search_query='100', chosen_option='equals to')
        self.assertEqual(qs.count(), self.number_of_records)
        qs = Record.objects.filter_quantity(search_query='99', chosen_option='more than')
        self.assertEqual(qs.count(), self.number_of_records)
        qs = Record.objects.filter_quantity(search_query='200', chosen_option='less than')
        self.assertEqual(qs.count(), self.number_of_records)
        qs = Record.objects.filter_quantity(search_query='1000', chosen_option='more than')
        self.assertNotEqual(qs.count(), self.number_of_records)

