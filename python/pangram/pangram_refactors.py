def is_pangram(sentence):
    letters_in_sentence = list(filter(str.isalpha, sentence.lower()))
    return 26 == len(set(letters_in_sentence))

# I also like this but it requires the imported String module:

import string
def is_pangram(sentence):
    alphabet = set(string.ascii_lowercase)
    return alphabet.issubset(sentence.lower())

