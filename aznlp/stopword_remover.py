from aznlp.letter_map import lower_map
from aznlp.words import stopwords


def remove_stopwords(sentence_with_stopwords):
    words_without_stopwords = [word for word in sentence_with_stopwords if word.translate(lower_map) not in stopwords]
    return words_without_stopwords
