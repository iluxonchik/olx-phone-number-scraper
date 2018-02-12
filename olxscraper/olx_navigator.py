from olxscraper.olx_listings import OlxListings
from olxscraper.product import Product
from olxscraper.requestor import Requestor
import time

class OlxNavigator(object):

    def __init__(self, listings_url, write_file_name = None, page_limit=None, number_limit=None):
        self._url = listings_url
        self._keep_scraping = True
        self._PAGE_LIMIT = page_limit
        self._PHONE_NUMBER_LIMIT = number_limit

        if write_file_name is not None:
            self._out_file = write_file_name
        else:
            self._out_file = '{}.txt'.format(str(int(time.time())))

        self._requestor = Requestor()

    def scrape_phone_numbers(self):
        """
        Go to listings url
        Get all listing_urls
        while there is a "Seguinte" span in HTML source:
            for listing_url in listing_urls:
                    go to listing_url
                    if listing_url has phone number:
                        get phone_number from listing_url
                        write phone_number to file
            go to next page
        """

        num_pages_scraped = 1
        num_numbers_scraped = 0

        print('Writing output to {}'.format(self._out_file))
        with open(self._out_file, mode='a') as out_file:
            while self._keep_scraping:

                olx = OlxListings(url=self._url)

                print('Scraping page #{}.{}'.format(num_pages_scraped, self._url))

                listing_urls = olx.get_listing_urls_from_page()
                for listing_url in listing_urls:
                    html = self._requestor.get_html_from_url(listing_url)
                    product = Product(html, listing_url)
                    if product.is_phone_number_present and self._keep_scraping:
                        phone_number_url = product.get_phone_number_url()
                        phone_number = product.get_phone_number(phone_number_url, listing_url)

                        self._write_phone_number_to_file(phone_number, out_file)

                        num_numbers_scraped += 1
                        print('\tScraped phone number #{}:{}'.format(num_numbers_scraped, phone_number))
                        self._check_phone_number_limit(num_numbers_scraped)

                next_page = olx.get_next_page_if_present()
                num_pages_scraped += 1
                self._check_page_number_limit(num_pages_scraped)

                if next_page is None:
                    self._keep_scraping = False
                    print('[DONE] Reached last page')
                else:
                    self._url = next_page

    def _write_phone_number_to_file(self, phone_number, out_file):
        out_file.write('{}\n'.format(phone_number))
        out_file.flush()

    def _check_phone_number_limit(self, num_numbers_scraped):
        if self._PHONE_NUMBER_LIMIT is None:
            return

        if num_numbers_scraped >= self._PHONE_NUMBER_LIMIT:
            print('[DONE] Stopping scraping due to phone number limit ({})'.format(self._PHONE_NUMBER_LIMIT))
            self._keep_scraping = False

    def _check_page_number_limit(self, num_pages_scraped):
        if self._PAGE_LIMIT is None:
            return

        if num_pages_scraped >= self._PAGE_LIMIT:
            print('[DONE] Stopping scraping due to page number limit ({})'.format(self._PAGE_LIMIT))
            self._keep_scraping = False
