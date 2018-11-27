import unittest
import os.path
from Cambridge import Cambridge
from os import remove


class TestCambridge(unittest.TestCase):

    def test_get_url_base(self):
        cambridge = Cambridge()
        url_base = cambridge.getUrlBase()
        self.assertEqual('https://dictionary.cambridge.org', url_base)

    def test_get_pronunciation_string(self):
        cambridge = Cambridge()
        cambridge.getWordData('luck')
        pronunciation = cambridge.getPronunciation()
        self.assertEqual('/lʌk/', pronunciation)

    def test_get_sound_file(self):
        path = './temp-downloads/'
        cambridge = Cambridge()
        cambridge.getWordData('luck')
        sound_file_path = path + cambridge.getSoundFile(path)
        self.assertTrue(os.path.exists(sound_file_path))
        remove(sound_file_path)

    def test_getWordData_for_bigger(self):
        cambridge = Cambridge()
        cambridge.getWordData('bigger')
        print(cambridge.getPronunciation())

if __name__ == '__main__':
    unittest.main()