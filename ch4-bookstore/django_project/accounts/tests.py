from django.contrib.auth import get_user_model
from django.test import TestCase

# As in Java, all has a class, like suggested by Bjarne and Martin but for Polymofirsms
class CustomUserTests(TestCase):
    """Tests for the custom user
    
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
