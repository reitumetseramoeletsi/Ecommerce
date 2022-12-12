from django.test import TestCase
from django.contrib.auth.models import User

from buildAstore.models import Category, Product

class TestCategoriesModel(TestCase):
    
    def setUp(self):
        self.data1 = Category.objects.create(name='home', slug='home')

    def test_category_model_return(self):
        """
        Test Category Model data insertion
        """
        data = self.data1
        self.assertTrue(isinstance(data, Category))

    def test_category_model_return(self):
        """
        Test if Category model return name
        """
        data = self.data1
        self.assertEqual(str(data), 'home')


class TestProductsModel(TestCase):

    def setUp(self):
        Category.objects.create(name='mats', slug='mats')
        User.objects.create(username='admin')
        self.data1 = Product.objects.create(Category_id=1, title='mats', created_by_id=1,
                                        slug='mats', price='20.00', image='mats')

    def test_products_model_return(self):
        """
        Test if Product model return attributes
        """
        data = self.data1
        self.assertTrue(isinstance(data, Product))
        self.assertEqual(str(data), 'mats')
        