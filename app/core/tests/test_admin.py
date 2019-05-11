from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse


class AdminSiteTests(TestCase):

    def setUp(self): # runs before everytests, setup
        self.client = Client() # client that makes request or uses webpage
        self.admin_user = get_user_model().objects.create_superuser(
            email='admin@londonappdev.com',
            password='password123'
        )
        self.client.force_login(self.admin_user) # client logins in as admin user
        self.user = get_user_model().objects.create_user(
            'test@londonappdev.com',
            'test123'
        )

    def test_users_listed(self):
        """ Test that users are listed on user page  """
        url = reverse('admin:core_user_changelist') # admin fields those links in django doc, app - admin - name of url
        res = self.client.get(url)

        self.assertContains(res, self.user.name)
        self.assertContains(res, self.user.email)

    def test_user_change_page(self):
        """ Test that the user edit page works """
        url = reverse('admin:core_user_change', args=[self.user.id])
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)

    def test_create_user_page(self):
        """ Test that the create user page works """
        url = reverse('admin:core_user_add')
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)
