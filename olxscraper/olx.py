import requests, re

class Olx(object):

    LINK_REGEX = r'detailsLink ( nophoto)?"(.|\n)*?href="(?P<listing_url>.+?)"'
    LINK_REGEX_WITH_PHOTOS_ONLY = r'detailsLink "(.|\n)*?href="(?P<listing_url>.+?)"'

    NEXT_PAGE_LINK_REGEX = r'href="(?P<next_page_url>.+?)">\n.*?<span>Seguinte'


    def __init__(self, url):
        self._url = url  # NEVER update URL directly!
        self._url_updated = False
        self._html = None

        self.link_pattern = re.compile(Olx.LINK_REGEX)
        self._next_page_link_pattern = re.compile(Olx.NEXT_PAGE_LINK_REGEX)

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
        pass

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

    def _get_next_page_if_present(self):

        self._update_html_from_curr_url()
        match = self._next_page_link_pattern.search(self._html)

        if match is None:
            return None
        else:
            return match.group('next_page_url')


    def _update_html_from_curr_url(self):
        if self._url_updated:
            return True

        # NOTE: dirty hack; needed for testing.
        if self._url.startswith('file://'):
            self._url = self._url[7:]  # remove the "file://" prefix
            with open(self._url, mode='r') as f:
                self._html = f.read()
        else:
            res = requests.get(self._url)
            self._html = res.text

        self._url_updated = True

    def _update_url(self, new_url):
        self._url = new_url
        self._url_updated = False
