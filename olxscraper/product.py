import re
from olxscraper.requestor import Requestor
from olxscraper.exceptions import (ListingIDNotFoundInURLException, PhoneTokenNotFoundException)
import json


class Product(object):

    PN_PRESENT_REGEX = r'contact-button link-phone'
    pn_present_pattern = re.compile(PN_PRESENT_REGEX)

    LISTING_ID_REGEX = r'ID(?P<listing_id>.+?)\.html'
    listing_id_pattern = re.compile(LISTING_ID_REGEX)

    PHONE_TOKEN_REGEX = r"var phoneToken = '(?P<phone_token>.+?)';"
    phone_token_pattern = re.compile(PHONE_TOKEN_REGEX)

    MULTIPLE_PHONE_NUMBERS_REGEX = r'(?P<phone_number>\d+?)<\/span>'
    multiple_phone_numbers_pattern = re.compile(MULTIPLE_PHONE_NUMBERS_REGEX)

    PHONE_NUMBER_URL_FORMAT = 'https://www.olx.pt/ajax/misc/contact/phone/{}/?pt={}'

    def __init__(self, content, url):
        self._content = content
        self._url = url

        self._requestor = Requestor()

    @property
    def is_phone_number_present(self):
        return self._is_phone_number_present()

    def get_phone_number_url(self):
        listing_id = self._get_listing_id_from_url()
        phone_token = self._get_phone_token()
        phone_number_url = Product.PHONE_NUMBER_URL_FORMAT.format(listing_id, phone_token)
        return phone_number_url

    def _is_phone_number_present(self):
        return Product.pn_present_pattern.search(self._content) is not None

    def _get_listing_id_from_url(self):
        res = Product.listing_id_pattern.search(self._url)

        if res is None:
            raise ListingIDNotFoundInURLException(url)

        listing_id = res.group('listing_id')
        return listing_id

    def _get_phone_token(self):
        res = Product.phone_token_pattern.search(self._content)

        if res is None:
            raise PhoneTokenNotFoundException()

        phone_token = res.group('phone_token')
        return phone_token

    def get_phone_number(self, phone_number_url, referer_header):
        html = self._requestor.get_html_from_url(phone_number_url, referer_header)

        try:
            response = json.loads(html)
        except json.decoder.JSONDecodeError:
            # TODO: investigate the cause of this failure
            error_msg = '{}:{}:{}\n\n\n\n\n'.format(phone_number_url, referer_header, html)
            with open('errors.txt', mode='a') as errors_file:
                errors_file.write(error_msg)
            return '000000000'

        phone_number_raw = response['value']
        phone_number = phone_number_raw.replace(' ', '')

        # if multiple phone numbers are returned, if yes, return first only
        res = self.multiple_phone_numbers_pattern.search(phone_number)
        if res is not None:
            print('[!!!] Multiple phone numbres found, returning first only')
            phone_number = res.group('phone_number')

        return phone_number
