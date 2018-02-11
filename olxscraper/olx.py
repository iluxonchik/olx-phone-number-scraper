import requests, re

class Olx(object):

    LINK_REGEX = r'detailsLink ( nophoto)?"(.|\n)*?href="(?P<listing_url>.+?)"'
    LINK_REGEX_WITH_PHOTOS_ONLY = r'detailsLink "(.|\n)*?href="(?P<listing_url>.+?)"'

    def __init__(self, url):
        self._url = url
        self.link_pattern = re.compile(Olx.LINK_REGEX)

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

        html = None

        # NOTE: dirty hack; needed for testing.
        if self._url.startswith('file://'):
            self._url = self._url[7:]  # remove the "file://" prefix
            with open(self._url, mode='r') as f:
                html = f.read()
        else:
            res = requests.get(self._url)
            html = res.text

        link_urls = []
        matches = self.link_pattern.finditer(html)

        for match in matches:
            link_urls += [match.group('listing_url')]

        return link_urls
