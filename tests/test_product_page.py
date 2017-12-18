"""
Product page related tests.
"""
import unittest

from olxscraper.product import Product

PRODUCTS_FILE_PATH_FMT = 'tests/resources/products/product_{}.html'

class ProductPageTestCase(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def _setup_product(self, product_file_path):
        product = None
        with open(product_file_path, mode='rb') as f:
            content = f.read()
            product = Product(content)
        return product

    def test_is_phone_number_present_TRUE(self):
        # test if a phone number is present on a page
        product_file_path = PRODUCTS_FILE_PATH_FMT.format('Y1')
        product = self._setup_product(product_file_path)
        is_present = product.is_phone_number_present
        self.assertTrue(is_present, 'Phone number should be marked as present'
                        ' but is not')

    def test_is_phone_number_present_FALSE(self):
        # test if a phone number is present on a page
        product_file_path = PRODUCTS_FILE_PATH_FMT.format('N1')
        product = self._setup_product(product_file_path)
        is_present = product.is_phone_number_present
        self.assertFalse(is_present, 'Phone number should be marked as not'
                         ' present, but it is')

    def test_build_phone_number_request_url(self):
        # test building XMLHttpRequest url where the phone number will be
        # requested
        self.skipTest('TBI')
        product_file_path = PRODUCTS_FILE_PATH_FMT.format('Y1')
        product = self._setup_product(product_file_path)
        expected_url = 'https://www.olx.pt/ajax/misc/contact/phone/AXuRv/?pt=d62b55bff0e896f432f5915da5cbb5759e757c2570f1f9ec7cc1e00b026e825e7c4585ec7b5b072cd8d343ce15fc9d7832073896fd1b9f66b0c428aa0f65e85d'
        obtained_url = product.get_phone_number_url()
        self.assertEqual(expected_url, obtained_url, 'Wrong phone num url parsed')
