from django.test import TestCase
from .models import Video

class VideoModelTestCase(TestCase):
    def setUp(self) -> None:
        Video.objects.create(title='This is my title')
    def test_valid_title(self) -> None:
        title = Video.objects.filter(title='This is my title')
        self.assertTrue(title.exists())
    def test_created_count(self) -> None:
        count = Video.objects.all()
        self.assertEqual(count.count(), 1)