from django.test import TestCase
from app.models import GoodReadsAudit


# Testing Model
class TestModels(TestCase):
    def setUp(self):
        self.obj1 = GoodReadsAudit.objects.create(title="A Song of Ice and Fire (A Song of Ice and Fire, #1-5)", average_rating="", ratings_count="", num_pages="", image_url="", publication_year="", authors="")
        self.obj2 = GoodReadsAudit.objects.create(title="title 2", average_rating="", ratings_count="", num_pages="", image_url="", publication_year="", authors="")
        self.obj3 = GoodReadsAudit.objects.create(title="The Godfather", average_rating="", ratings_count="", num_pages="", image_url="", publication_year="", authors="")
        
    def test_weatheraudit_is_assigned_title_on_creation(self):
        self.assertEqual(self.obj1.title, 'A Song of Ice and Fire (A Song of Ice and Fire, #1-5)')
        self.assertEqual(self.obj2.title, 'title 2')
        self.assertEqual(self.obj3.title, 'The Godfather')

# Testing Url
class TestUrls(TestCase):
    pass