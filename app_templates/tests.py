from django.test import TestCase
from django.urls import reverse
from .models import Post
from datetime import date

class WeatherTests(TestCase):

    def test_home_page_status_code(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)

    def test_home_page_contains_table_headers(self):
        response = self.client.get(reverse("home"))
        self.assertContains(response, "Атмосферні вимірювання")

    def test_model_post_str(self):
        p = Post.objects.create(
            date=date(2026, 1, 1),
            temperature=0,
            pressure=750,
            wind_speed=2,
            precipitation=10
        )
        self.assertEqual(str(p), "2026-01-01")
