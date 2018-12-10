from Dictionary import Dictionary


class Cambridge(Dictionary):

    def __init__(self):
        self.search_url = 'https://dictionary.cambridge.org/dictionary/english/'

    def getPronunciation(self):
        body = self.getBody()
        ipa_span_list = body.select('.us .pron .ipa')

        if len(ipa_span_list) > 0:
            ipa_span = ipa_span_list[0]
            return '/' + ipa_span.get_text() + '/'

        return ''

    def getSoundFile(self, path):
        body = self.getBody()
        body_selection = body.select('.pron-info .us .circle')

        if len(body_selection) > 0:
            audio_play_button_span = body_selection[0]
            sound_file_url = self.getUrlBase() + audio_play_button_span['data-src-mp3']
            soud_file_name = self.word + '.mp3'
            self.downloadFile(sound_file_url, path + soud_file_name)
            return soud_file_name

        return ''