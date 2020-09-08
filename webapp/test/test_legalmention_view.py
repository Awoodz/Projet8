from django.test import TestCase
from django.urls import reverse


class LegalMentionPageTestCase(TestCase):
    def test_legal_mention_returns_200(self):
        response = self.client.get(reverse("legalmention"))
        self.assertEqual(response.status_code, 200)
