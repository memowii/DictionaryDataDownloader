from requests import get
from bs4 import BeautifulSoup as BS
from urllib.parse import urlparse
import urllib.request

class Dictionary:
    HEADERS = {'User-Agent': 'Chrome/68.0.3440.84'}
    dictionary_url = None

    def getWordData(self, word):
        self.word = word
        self.base_url = self.getUrlBase()
        self.page_content = self.getPageContent()
        self.soup = self.getSoup()
        self.html = self.getHtml()
        self.body = self.getBody()

    def getUrlBase(self):
        parse_result = urlparse(self.dictionary_url)
        return parse_result.scheme + '://' + parse_result.netloc

    def getPageContent(self):
        page = get(self.dictionary_url + self.word, headers=self.HEADERS)

        if page.status_code == 200:
            return page.content
        else:
            raise ValueError('Failure when getting web page for word {}'.format(word))

    def getSoup(self):
        if self.page_content:
            return BS(self.page_content, 'html.parser')

    def getHtml(self):
        return list(self.soup.children)[2]

    def getBody(self):
        return list(self.html.children)[3]

    def downloadFile(self, url_file, path_name):
        urllib.request.urlretrieve(url_file, path_name)
