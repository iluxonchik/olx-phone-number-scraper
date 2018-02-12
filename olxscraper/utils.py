import requests

REQUESTS_PER_SESSION = 80
CURR_SESSION_REQEUSTS = 0  # trigger session init on first run

session = None

def init_session():
    global session

    session = requests.Session()

    # NOTE: referer header is required!
    # NOTE: the only required cookeis are: PHPSESSID and pt
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36",
        "Accept": "*/*",
        "Accept-Encoding":"gzip, deflate, br",
        "X-Requested-With": "XMLHttpRequest"
    }

    session.headers.update(headers)

    # conenct to olx in order to get the cookies, which will be sent on
    # subsequent requests
    res = session.get('https://olx.pt')

init_session()

def check_session_requests_limit():
    global CURR_SESSION_REQEUSTS, REQUESTS_PER_SESSION

    if CURR_SESSION_REQEUSTS >= REQUESTS_PER_SESSION:
        print('[INFO] Resetting session...')
        init_session()
        CURR_SESSION_REQEUSTS = 0

    CURR_SESSION_REQEUSTS += 1


def get_html_from_url(url, referer_header="https://olx.pt/"):
    global session
    session.headers.update({"Referer":referer_header})
    html = None
    # NOTE: dirty hack; needed for testing.
    if url.startswith('file://'):
        url = url[7:]  # remove the "file://" prefix
        with open(url, mode='r') as f:
            html = f.read()
    else:
        res = session.get(url)
        html = res.text
    check_session_requests_limit()
    return html
