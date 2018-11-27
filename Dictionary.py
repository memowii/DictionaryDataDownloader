from requests import get
from bs4 import BeautifulSoup as BS
from urllib.parse import urlparse
import urllib.request

class Dictionary:
    HEADERS = {'User-Agent': 'Chrome/68.0.3440.84'}
    search_url = ''

    def getWordData(self, word):
        self.word = word
        self.page_content = self.getPageContent()
        self.soup = self.getSoup()

    def getUrlBase(self):
        parse_result = urlparse(self.search_url)
        return parse_result.scheme + '://' + parse_result.netloc

    def getPageContent(self):
        page = get(self.search_url + self.word, headers=self.HEADERS)

        if page.status_code == 200:
            return page.content
        else:
            raise ValueError('Failure when getting web page for word {}'.format(self.word))

    def getSoup(self):
        if self.page_content:
            return BS(self.page_content, 'html.parser')

    def getHtml(self):
        return self.soup.html

    def getBody(self):
        return self.soup.html.body

    def downloadFile(self, url_file, path_with_name):
        urllib.request.urlretrieve(url_file, path_with_name)
x
    def