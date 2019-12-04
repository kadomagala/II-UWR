from bs4 import BeautifulSoup
import requests
import re
from urllib.parse import urlparse


def get_links_from_url(html_doc, url):
    result = list()
    soup = BeautifulSoup(html_doc, 'html.parser')
    for link in soup.findAll('a', attrs={'href': re.compile("^http?://")}):
        result.append(link.get('href'))
    for link in soup.findAll('a', attrs={'href': re.compile("^/\w")}):
        result.append(get_url_domain(url)+link.get('href'))

    return result


def get_url_domain(url):
    parsed_uri = urlparse(url)
    result = '{uri.scheme}://{uri.netloc}'.format(uri=parsed_uri)
    return result


links_set = set()


def crawl(start_page, distance, action):
    url = None
    try:
        url = requests.get(start_page)
    except requests.exceptions.RequestException as e:
        print(e)
        yield ("Error", "Error")
        return
    html_doc = url.text
    result = action(html_doc)
    url.close()
    yield (start_page, result)

    if distance > 0:
        links = get_links_from_url(html_doc, start_page)
        links = list(filter(lambda l: l not in links_set, links))
        for link in links:
            links_set.add(link)
        for link in links:
            for p in crawl(link, distance-1, action):
                yield p


def find_python(html_doc):
    return 'Python' in html_doc


url = "http://ii.uni.wroc.pl/~marcinm/dyd/python/"
test = crawl(url, 2, find_python)

for s in test:
    print(s)
