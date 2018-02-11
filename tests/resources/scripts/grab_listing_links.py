"""
Grabs all listing urls from a page and returs them as a Python list (in a string).

Useful to automate link grabbing for testing.
"""

import sys, re
import pyperclip

LINK_REGEX = r'detailsLink ( nophoto)?"(.|\n)*?href="(?P<listing_url>.+?)"'
LINK_REGEX_WITH_PHOTOS_ONLY = r'detailsLink "(.|\n)*?href="(?P<listing_url>.+?)"'
link_pattern = re.compile(LINK_REGEX)

if len(sys.argv) < 2:
    print('Usage: {} FILE_NAME'.format(sys.argv[0]))
    sys.exit(0)
else:
    FILE_PATH = sys.argv[1]

with open(FILE_PATH, mode='r') as f:
    file_content = f.read()
    matches = link_pattern.finditer(file_content)

    link_urls = []

    for match in matches:
        link_urls += [match.group('listing_url')]

    list_size = len(link_urls)
    joined_urls = ', '.join(link_urls)

    str_list = '[{}]'.format(joined_urls)
    pyperclip.copy(str_list)
    print(str_list)
    print('\nThe text above has been copied to your clipboard.')
