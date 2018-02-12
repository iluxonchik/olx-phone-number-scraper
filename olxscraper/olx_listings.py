import re
from olxscraper.product import Product
from olxscraper.requestor import Requestor

class OlxListings(object):

    LINK_REGEX = r'detailsLink ( nophoto)?"(.|\n)*?href="(?P<listing_url>.+?)"'
    LINK_REGEX_WITH_PHOTOS_ONLY = r'detailsLink "(.|\n)*?href="(?P<listing_url>.+?)"'

    NEXT_PAGE_LINK_REGEX = r'href="(?P<next_page_url>.+?)">\n.*?<span>Seguinte'


    def __init__(self, url):
        self._url = url  # NEVER update URL directly!
        self._url_updated = False
        self._html = None

        self.link_pattern = re.compile(OlxListings.LINK_REGEX)
        self._next_page_link_pattern = re.compile(OlxListings.NEXT_PAGE_LINK_REGEX)

        self._requestor = Requestor()

    def get_listing_urls_from_page(self):
        """
        Returns a list of all of the listing URLs found on a page.
        """

        self._update_html_from_curr_url()

        link_urls = []
        matches = self.link_pattern.finditer(self._html)

        for match in matches:
            link_urls += [match.group('listing_url')]

        return link_urls


    def get_next_page_if_present(self):

        self._update_html_from_curr_url()
        match = self._next_page_link_pattern.search(self._html)

        if match is None:
            return None
        else:
            return match.group('next_page_url')

    def _update_html_from_curr_url(self):
        if self._url_updated:
            return True

        self._html = self._requestor.get_html_from_url(self._url)

        self._url_updated = True
