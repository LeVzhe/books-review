from rest_framework.test import APITestCase

from users.models import User


class UserAuthTests(APITestCase):

    def setUp(self):
        user_test1 = User.objects.create(
            username="TestUser1",
            email="test@user1.com",
            password="Testuser123",
        )
        user_test1.save()
        user_test2 = User.objects.create(
            username="TestUser2",
            email="test@user2.com",
            password="Testuser223",
        )
        user_test2.save()
        user_test3 = User.objects.create(
            username="TestUser3",
            email="test@user3.com",
            password="Testuser323",
        )
        user_test3.save()
