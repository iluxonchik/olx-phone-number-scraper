""" requests.session wrapper for Olx scraping """

import requests
from olxscraper.decorators import singleton

@singleton
class Requestor(object):
    """
    Wrapper arround requests.session that implements olx scraper specific
    functionality, such as cookie setting, required header placement and
    automatic session resetting.
    """

    def __init__(self, requests_per_session = 80):
        self._REQUESTS_PER_SESSION = requests_per_session
        self._CURR_SESSION_REQUESTS = 0

        print('Initting session...')
        self._init_session()

    def _init_session(self):
        self._session = requests.Session()

        # NOTE: referer header is required!
        # NOTE: the only required cookeis are: PHPSESSID and pt
        headers = {
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36",
            "Accept": "*/*",
            "Accept-Encoding":"gzip, deflate, br",
            "X-Requested-With": "XMLHttpRequest"
        }

        self._session.headers.update(headers)

        # conenct to olx in order to get the cookies, which will be sent on
        # subsequent requests
        self._session.get('https://olx.pt')

    def _update_session_if_needed(self):
        if self._CURR_SESSION_REQUESTS >= self._REQUESTS_PER_SESSION:
            print('[INFO] Resetting session due to requests limit...')
            self._CURR_SESSION_REQUESTS = 0
            self._init_session()
        else:
            self._CURR_SESSION_REQUESTS += 1

    def get_html_from_url(self, url, referer_header='https://olx.pt'):
        self._session.headers.update({"Referer":referer_header})
        html = None
        # NOTE: dirty hack; needed for testing.
        if url.startswith('file://'):
            url = url[7:]  # remove the "file://" prefix
            with open(url, mode='r') as f:
                html = f.read()
        else:
            res = self._session.get(url)
            html = res.text
            self._update_session_if_needed()
        return html
