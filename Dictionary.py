from requests import get
from bs4 import BeautifulSoup as BS

class Dictionary:
    HEADERS = {'User-Agent': 'Chrome/68.0.3440.84'}

    def __init__(self, dictionary_url):
        self.dictionary_url = dictionary_url

    def getPageContent(self, word):
        page = get(self.dictionary_url + word, headers=self.HEADERS)

        if page.status_code == 200:
            return page.content

        raise ValueError('Failure when getting web page for word {}'.format(word))

    def getSoup(self, page_content):
        if page_content:
            return BS(page_content, 'html.parser')

    def getHtml(self, soup):
        return list(soup.children)[2]

    def getBody(self, html):
        return list(html.children)[3]

    def getPronunciation(self, word):
        page_content = self.getPageContent(word)
        soup = self.getSoup(page_content)
        html = self.getHtml(soup)
        body = self.getBody(html)

        return body.prettify()