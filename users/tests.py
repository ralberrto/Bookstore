from django.contrib.auth import get_user_model
from django.test import TestCase


class CustomUserTests(TestCase):
    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            username="will",
            email="will@email.com",
            password="testpassword123\;",
        )
        self.assertEqual(user.username, "will")
        self.assertEqual(user.email, "will@email.com")
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        User = get_user_model()
        superuser = User.objects.create_superuser(
            username="superadmin",
            email="superadmin@email.com",
            password="takes%%12!0",
        )
        self.assertEqual(superuser.username, "superadmin")
        self.assertEqual(superuser.email, "superadmin@email.com")
        self.assertTrue(superuser.is_active)
        self.assertTrue(superuser.is_staff)
        self.assertTrue(superuser.is_superuser)