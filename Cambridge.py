from Dictionary import Dictionary


class Cambridge(Dictionary):

    def __init__(self):
        self.search_url = 'https://dictionary.cambridge.org/dictionary/english/'

    def getPronunciation(self):
        ipa_span = self.body.select('.us .pron .ipa')[0]

        if ipa_span:
            return '/' + ipa_span.get_text() + '/'
        return ''

    def getSoundFile(self, path):
        span_audio_play_button = self.body.select('.pron-info .us .circle')[0]
        sound_file_url = self.base_url + span_audio_play_button['data-src-mp3']
        soud_file_name = self.word + '.mp3'
        self.downloadFile(sound_file_url, path + soud_file_name)
        return soud_file_name
