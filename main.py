from Dictionary import Dictionary
from DB import DB

cambridge_dictionary = Dictionary('https://dictionary.cambridge.org/dictionary/english/')
db = DB()
duolingo_words = db.getAllDuolingoWords()

for duolingo_word in duolingo_words:
    print(duolingo_word)
    cambridge_dictionary.getWordData(duolingo_word['word'])
    pronunciation = cambridge_dictionary.getPronunciation()
    sound_file = cambridge_dictionary.getSoundFile()
    db.updatePronAndSoundFile(duolingo_word['id'],
                              pronunciation,
                              sound_file)
    break


exit(11)

cambridge_dictionary.getWordData('luck')
cambridge_dictionary.getSoundFile()



# TODO: aplicar threads in duolingo_words.py para hacerlo mas rapido