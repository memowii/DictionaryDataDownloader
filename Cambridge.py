from Dictionary import Dictionary


class Cambridge(Dictionary):

    def __init__(self):
        self.search_url = 'https://dictionary.cambridge.org/dictionary/english/'

    def getPronunciation(self):
        body = self.getBody()
        ipa_span = body.select('.us .pron .ipa')[0]

        if ipa_span:
            return '/' + ipa_span.get_text() + '/'
        return ''

    def getSoundFile(self, path):
        body = self.getBody()
        audio_play_button_span = body.select('.pron-info .us .circle')[0]
        sound_file_url = self.getUrlBase() + audio_play_button_span['data-src-mp3']
        soud_file_name = self.word + '.mp3'
        self.downloadFile(sound_file_url, path + soud_file_name)
        return soud_file_name
