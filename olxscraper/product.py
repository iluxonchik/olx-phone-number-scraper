import re

class Product(object):

    PN_PRESENT_REGEX = rb'contact-button link-phone'
    pn_present_pattern = re.compile(PN_PRESENT_REGEX)

    def __init__(self, content):
        self._content = content

    @property
    def is_phone_number_present(self):
        return self._is_phone_number_present()

    def _is_phone_number_present(self):
        return Product.pn_present_pattern.search(self._content) is not None
