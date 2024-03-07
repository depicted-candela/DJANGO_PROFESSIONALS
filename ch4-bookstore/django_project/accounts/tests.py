from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse, resolve

from .forms import CustomUserCreationForm
from .views import SignUpPageView

# As in Java, all has a class, like suggested by Bjarne and Martin but for Polymofirsms
class CustomUserTests(TestCase):
    """Tests for the custom user. This series of tests are needed since CustomUser is not a default class provided by Django
    
    Args:
        TestCase (TestCase): The TestCase class from django.test provides a base for Django unit tests, automatically setting up a clean database for each test and allowing database interactions for testing data manipulation and model behavior.
    """
    def test_create_user(self):
        """To test the capability for creating custom users
        """
        User = get_user_model()
        user = User.objects.create_user(
            username="christov", email="christov@gmail.com", password="123"
        )
        self.assertEqual(user.username, "christov")
        self.assertEqual(user.email, "christov@gmail.com")
        self.assertTrue(user.is_active)
        # Because since the user is fot custom users the constructor
        # does not have the args for staff and superuser
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)
    def test_create_superuser(self):
        """To test the capability for editing custom users
        """
        User = get_user_model()
        admin_user = User.objects.create_superuser(
            username="admin", email="admin@gmail.com", password="admin123"
        )
        self.assertEqual(admin_user.username, "admin")
        self.assertEqual(admin_user.email, "admin@gmail.com")
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)

class SignUpPageTests(TestCase):
    """This class makes the tests for the accounts/signup/ page

    Args:
        TestCase (TestCase): The TestCase class from django.test provides a base for Django unit tests, automatically setting up a clean database for each test and allowing database interactions for testing data manipulation and model behavior.
    """
    def setUp(self):
        """The custom Django initializer, here takes the same response but with two different ways
        """
        self.response = self.client.get(reverse("signup"))
    
    def test_url(self):
        """Test if url catching is satisfactory
        """
        self.assertEqual(self.response.status_code, 200)
    
    def test_template(self):
        """Test if the template rendered by the view is registration/signup.html, as should be
        """
        self.assertTemplateUsed(self.response, "registration/signup.html")
        self.assertContains(self.response, "The page for Signing Up")
        self.assertNotContains(self.response, "The page for Signing Upp")
    
    def test_form(self):
        """Test if the form rendered by the given url is the desired to be there
        """
        form = self.response.context.get("signup-form")
        self.assertContains(self.response, "signup-form")
        self.assertIsInstance(form, CustomUserCreationForm) # Makes a comparison between the form contained by the get method
                                                            # specified in the form_class variable of the SignUpPage view
        self.assertContains(self.response, "csrfmiddlewaretoken")
                                                            # Since a needed transferring data is security, middleware tokens for
                                                            # csrf should tested by asserting that the response is containing it
        # All sets are based on needs per feature
    
    def test_view(self):
        """To know if the name of the view in the url is really the name of SignUpPageView
        """
        view = resolve("/accounts/signup/")                  # Get temporarily the view in the /accounts/signup url
        self.assertEqual(view.func.__name__, SignUpPageView.as_view().__name__)
