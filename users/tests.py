from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from users.models import User


class UsersTestCase(APITestCase):
    """Тестирование пользователей"""

    def setUp(self):
        self.user = User.objects.create(email="test@example.com")
        self.user.set_password("123")
        self.user.save()
        self.client.force_authenticate(user=self.user)

    def test_user_create(self):
        url = reverse("users:user_register")
        data = {
            "email": "test1@example.com",
            "password": "12345",
        }
        response = self.client.post(url, data=data)
        print("Пользователь создан")
        print(response.json())
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.all().count(), 2)
