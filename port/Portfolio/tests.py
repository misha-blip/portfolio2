from django.test import TestCase


class HomePageTest(TestCase):

    def test_home_page_status_code(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)


class PollsPageTest(TestCase):

    def test_polis_page_status_code(self):
        response = self.client.get("/polls/")
        self.assertEqual(response.status_code, 200)