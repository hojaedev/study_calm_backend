from django.test import TestCase
from accounts.models import User, UserAccountManager


class UserTestCase(TestCase):
    pass

class AuthTestCase(TestCase):
    def setUp(self):
        user = UserAccountManager.create_superuser('admin1@gmail.com',password='pass')
        # user.is_active = True
        user.save()

    def testLogin(self):
        self.client.login(username='admin1@gmail.com', password='pass')
