from Cambridge import Cambridge
from DB import DB
from time import sleep

cambridge_dictionary = Cambridge()
db = DB()
duolingo_words = db.getAllDuolingoWords()

for duolingo_word in duolingo_words:
    if len(duolingo_word['word'].split(' ')) == 1 and duolingo_word['word'].find("'") == -1 and duolingo_word['id'] >= 36:
        cambridge_dictionary.getWordData(duolingo_word['word'])
        word_pronunciation = cambridge_dictionary.getPronunciation()
        db.updatePronAndSoundFile(duolingo_word['id'], word_pronunciation)
        cambridge_dictionary.getSoundFile('./resources/cambridge_dictionary/')
        sleep(1)

# TODO: aplicar threads in duolingo_words.py para hacerlo mas rapido
# TODO: utilizar algo para alchemy para la base de datos
# TODO: utilizar nltk para hacer las busquedas más simples