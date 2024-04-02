from django.test import TestCase
from django.urls import reverse


class HomePageTest(TestCase):
    def test_home_url(self):
        res = self.client.get('')
        self.assertEqual(res.status_code, 200)

    def test_home_url_by_name(self):
        res = self.client.get(reverse('home'))
        self.assertEqual(res.status_code, 200)

    def test_home_content(self):
        res = self.client.get(reverse('home'))
        self.assertContains(res, 'Home')

    def test_home_template(self):
        res = self.client.get(reverse('home'))
        self.assertTemplateUsed(res, 'home.html')


class AboutUsTest(TestCase):
    def test_aboutus_url(self):
        res = self.client.get('/aboutus/')
        self.assertEqual(res.status_code, 200)

    def test_aboutus_url_by_name(self):
        res = self.client.get(reverse('aboutus'))
        self.assertEqual(res.status_code, 200)

    def test_aboutus_content(self):
        res = self.client.get(reverse('aboutus'))
        self.assertContains(res, 'about')

    def test_aboutus_template(self):
        res = self.client.get(reverse('aboutus'))
        self.assertTemplateUsed(res, 'pages/about.html')
