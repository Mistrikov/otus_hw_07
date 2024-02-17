# from django.test import TestCase
from rest_framework.test import APITestCase, APIClient, APISimpleTestCase
from userapp.models import ScUser

# TestCase работает с базой
# SimpleTestCase без базы
# APISimpleTestCase без базы
# APITestCase c базой
# APIRequestFactory - эмулирует запросы
# RequestClient, CoreAPIClient - реальные запросы


class CategoryCourseViewSetTestCase(APITestCase):
    def setUp(self):
        self.url = '/api/category/'
        self.user = ScUser.objects.create_user('test', 'test@qw.com', '1')
        self.auth_client = APIClient()

    def test_get(self):
        res = self.auth_client.get(self.url)
        self.assertEqual(res.status_code, 403)

        self.auth_client.force_authenticate(user=self.user)
        res = self.auth_client.get(self.url)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.data['results'], [])
        self.assertTrue(isinstance(res.content, bytes))

    """def test_create(self):
        data = {
            'name': 'Тестовая категория',
            'description': 'Описание тестовой категории'
        }
        res = self.client.post(self.url, data=data)
        self.assertEqual(res.status_code, 201)"""


class RandomTestCase(APISimpleTestCase):
    def setUp(self):
        self.url = '/api/randomnumber/'
        self.res = self.client.get(self.url)

    """def test_status_code(self):
        # плохой способ
        rand_num = self.res.data['random_number']
        self.assertIn(rand_num, [1, 2])

        # mock"""
