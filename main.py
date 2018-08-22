from Dictionary import Dictionary
from requests import get

# cambridge_dictionary = Dictionary('https://dictionary.cambridge.org/dictionary/english/')
cambridge_dictionary = Dictionary('https://dictionary.cambridge.org/dictionary/english/')

print(cambridge_dictionary.getPronunciation('luck'))
# print(cambridge_dictionary.getPronunciation('dog'))

# cambridge_dictionary.getPronunciation('luck') # publico
# cambridge_dictionary.getSoundFile('luck')   # public
#
# print(cambridge_dictionary.getWordPage('luck'))


# page = get('http://www.wordreference.com/definition/luck')
# print(page.content)



# TODO: aplicar threads in duolingo_words.py para hacerlo mas rapido