import unittest
import os.path
from WordReference import WordReference
from os import remove


class TestCambridge(unittest.TestCase):

    def test_get_url_base(self):
        word_reference = WordReference()
        url_base = word_reference.getUrlBase()
        self.assertEqual('http://www.wordreference.com', url_base)

    def test_get_pronunciation_string(self):
        word_reference = WordReference()
        word_reference.getWordData('luck')
        pronunciation = word_reference.getPronunciation()
        self.assertEqual('/lʌk/', pronunciation)


if __name__ == '__main__':
    unittest.main()