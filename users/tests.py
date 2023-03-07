from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse, resolve

from .views import SignupPageView
from .forms import CustomUserCreationForm


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


class SignupPageTests(TestCase):
    def setUp(self):
        url = reverse("signup")
        self.response = self.client.get(url)

    def test_signup_template(self):
        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateUsed(self.response, "registration/signup.html")
        self.assertContains(self.response, "Sign Up")
        self.assertNotContains(self.response, "Hi there! I probably shouldn't be on the page!")

    def test_signup_form(self):
        form = self.response.context.get("form")
        self.assertIsInstance(form, CustomUserCreationForm)
        self.assertContains(self.response, "csrfmiddlewaretoken")

    def test_signup_view(self):
        view = resolve("/users/signup/")
        self.assertEqual(view.func.__name__, SignupPageView.as_view().__name__)