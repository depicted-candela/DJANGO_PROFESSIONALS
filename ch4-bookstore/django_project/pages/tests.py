from django.test import SimpleTestCase
from django.urls import reverse, resolve
from .views import HomePageView

class HomepageTests(SimpleTestCase):
    """Class for testing the pages App

    Args:
        SimpleTestCase (SimpleTestCase): inherited lightweight base class for writing tests that don't involve interacting with the database
    """
    def setUp(self):
        """A sort of constructor. To get a response getting, from the client, the home url "/".
        Not used the 

        Returns:
            HttpRequest: response of the home url "/"
        """
        self.response = self.client.get(reverse("home")) # This code is telling a story
        self.url_response = self.client.get("/") # counterintuitive but is for test a url
    def test_homepage_url(self):
        """tests if the "/" (with name as home) url exists
        """
        self.assertEqual(self.response.status_code, 200)
    def test_url_exists_at_correct_location(self):
        """tests if the "/" url exists
        """
        self.assertEqual(self.url_response.status_code, 200)
    def test_homepage_template(self):
        """tests if the template for the "/" (with name as home) url exists
        """
        self.assertTemplateUsed(self.response, "home.html")
    def test_homepage_contains_correct_html(self):
        """tests if the html of the given url or name contains some correct text
        """
        self.assertContains(self.response, "is our")
    def test_homepage_does_not_contains_incorrect_html(self):
        """tests if the html of the given url or name not contains some incorrect text
        """
        self.assertNotContains(self.response, "an incorrect code")
    def test_homepage_url_resolves_homepageview(self):
        """test if the view HomePageView is the same as the rendered by the "/" url catched with the resolve() method
        """
        view = resolve("/")
        self.assertEqual(view.func.__name__, HomePageView.as_view().__name__)