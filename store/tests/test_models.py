from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from store.models import Category, Course


class TestCategoriesModel(TestCase):

    def setUp(self):
        self.data1 = Category.objects.create(name='django', slug='django')

    def test_category_model_entry(self):
        """
        Test Category model data insertion/types/field attributes
        """
        data = self.data1
        self.assertTrue(isinstance(data, Category))
        self.assertEqual(str(data), 'django')

    def test_category_url(self):
        """
        Test category model slug and URL reverse
        """
        data = self.data1
        response = self.client.post(
            reverse('store:category_list', args=[data.slug]))
        self.assertEqual(response.status_code, 200)


class TestcoursesModel(TestCase):
    def setUp(self):
        Category.objects.create(name='django', slug='django')
        User.objects.create(username='admin')
        self.data1 = Course.objects.create(category_id=1, title='django beginners', created_by_id=1,
                                           slug='django-beginners', price='100000', image='django')
        self.data2 = Course.courses.create(category_id=1, title='django advanced', created_by_id=1,
                                           slug='django-advanced', price='100000', image='django', is_active=False)

    def test_courses_model_entry(self):
        """
        Test course model data insertion/types/field attributes
        """
        data = self.data1
        self.assertTrue(isinstance(data, Course))
        self.assertEqual(str(data), 'django beginners')

    def test_courses_url(self):
        """
        Test course model slug and URL reverse
        """
        data = self.data1
        url = reverse('store:course_detail', args=[data.slug])
        self.assertEqual(url, '/django-beginners')
        response = self.client.post(
            reverse('store:course_detail', args=[data.slug]))
        self.assertEqual(response.status_code, 200)

    def test_courses_custom_manager_basic(self):
        """
        Test course model custom manager returns only active courses
        """
        data = Course.courses.all()
        self.assertEqual(data.count(), 1)
