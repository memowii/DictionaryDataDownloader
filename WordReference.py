from Dictionary import Dictionary


class WordReference(Dictionary):

    def __init__(self):
        self.search_url = 'http://www.wordreference.com/definition/'

    def getPronunciation(self):
        body = self.getBody()
        ipa_span = body.select('#pronWR')[0]
        pronunciation_word_reference = ipa_span.get_text()
        pronunciation = pronunciation_word_reference.split(' ')[1]
        if pronunciation:
            return pronunciation
        return ''

    def getSoundFile(self, path):
        body = self.getBody()

        span_audio_play_button = body.select('.pron-info .us .circle')[0]
        sound_file_url = self.base_url + span_audio_play_button['data-src-mp3']
        soud_file_name = self.word + '.mp3'
        self.downloadFile(sound_file_url, path + soud_file_name)
        return soud_file_name
