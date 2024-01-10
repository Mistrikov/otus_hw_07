from django.test import TestCase
from .models import CategoryCourse

class TestCategoryCourse(TestCase):
    def test_some(self):
        self.assertEqual(1, 1)

    def test_str(self):
        category = CategoryCourse.objects.create(name='QW')
        self.assertEqual(category.name, 'QW')

class TestCategoryCourseListView(TestCase):
    def test_status_code(self):
        url = '/categorycourse/list/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_context(self):
        url = '/categorycourse/list/'
        response = self.client.get(url)
        context = response.context
        self.assertIn('object_list', context)
        category_list = context['object_list']
        self.assertEqual(len(category_list), 0)

        category = CategoryCourse.objects.create(name='My category')
        response = self.client.get(url)
        context = response.context
        pass

        
