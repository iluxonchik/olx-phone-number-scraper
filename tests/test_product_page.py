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

    def _setup_product(self, product_file_path, url):
        product = None
        with open(product_file_path, mode='r') as f:
            content = f.read()
            product = Product(content, url)
        return product

    def test_is_phone_number_present_TRUE(self):
        # test if a phone number is present on a page
        product_file_path = PRODUCTS_FILE_PATH_FMT.format('Y1')
        product = self._setup_product(product_file_path, None)
        is_present = product.is_phone_number_present
        self.assertTrue(is_present, 'Phone number should be marked as present'
                        ' but is not')

    def test_is_phone_number_present_FALSE(self):
        # test if a phone number is present on a page
        product_file_path = PRODUCTS_FILE_PATH_FMT.format('N1')
        product = self._setup_product(product_file_path, None)
        is_present = product.is_phone_number_present
        self.assertFalse(is_present, 'Phone number should be marked as not'
                         ' present, but it is')

    def test_build_phone_number_request_url(self):
        # test building XMLHttpRequest url where the phone number will be
        # requested
        product_file_path = PRODUCTS_FILE_PATH_FMT.format('Y1')
        product = self._setup_product(product_file_path, 'https://www.olx.pt/anuncio/vendo-capa-apple-verde-iphone-6-6s-plus-IDAXuRv.html')

        # First, let's make sure that the listing ID was parsed correctly
        expected_listing_id = 'AXuRv'
        obtained_listing_id = product._get_listing_id_from_url()
        self.assertEqual(expected_listing_id, obtained_listing_id,
                         'Wrong listing ID parsed')

        # Now let's make sure that the phoneToken was parsed correctly
        expected_phone_token = '7d6a8bf435f2fd90908ffc262c80a280574d0c73148eeac546a40b4356d5455189b558545392be7f4f216d668171334eda00f82ec577ef80d65a5542756858e5'
        obtained_phone_token = product._get_phone_token()
        self.assertEqual(expected_phone_token, obtained_phone_token,
                         'Wrong phoneToken parsed')

        # Finally, let's test that the final url was built correctly
        expected_url = 'https://www.olx.pt/ajax/misc/contact/phone/AXuRv/?pt=7d6a8bf435f2fd90908ffc262c80a280574d0c73148eeac546a40b4356d5455189b558545392be7f4f216d668171334eda00f82ec577ef80d65a5542756858e5'
        obtained_url = product.get_phone_number_url()
        self.assertEqual(expected_url, obtained_url, 'Wrong phone num url parsed')
