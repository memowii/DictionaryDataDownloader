from Dictionary import Dictionary

class Cambridge(Dictionary):

    def __init__(self):
        self.dictionary_url = 'https://dictionary.cambridge.org/dictionary/english/'

    def getPronunciation(self):
        ipa_span = self.body.select('.us .pron .ipa')[0]

        if ipa_span:
            return '/' + ipa_span.get_text() + '/'
        return ''

    def getSoundFile(self):
        span_audio_play_button = self.body.select('.pron-info .us .circle')[0]
        sound_file_url = self.base_url + span_audio_play_button['data-src-mp3']
        self.downloadFile(sound_file_url,
                          './resources/cambridge_dictionary/' + self.word + '.mp3')
        return self.word + '.mp3'
