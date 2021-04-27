from aznlp.azerbaijani_lemmatizer import AzerbaijaniLemmatizer
from aznlp import word_noise_remover
from aznlp import stopword_remover


def clean_tokens(category_tokens):
    # print(category_tokens)
    clean_words = [word_noise_remover.remove_noise(word) for word in category_tokens]
    # print(clean_words)
    lemmatizer = AzerbaijaniLemmatizer()
    lemmata = lemmatizer.lemmatize(clean_words)
    lemmata_without_stopwords = stopword_remover.remove_stopwords(lemmata)
    cleaned_tokens = []
    for lemma in lemmata_without_stopwords:
        cleaned_tokens.append(lemma)

    return cleaned_tokens


def clean_tokens_stopwords(category_tokens):
    # print(category_tokens)
    clean_words = [word_noise_remover.remove_noise(word) for word in category_tokens]
    # print(clean_words)
    lemmatizer = AzerbaijaniLemmatizer()
    lemmata = lemmatizer.lemmatize(clean_words)
    # lemmata_without_stopwords = stopword_remover.remove_stopwords(lemmata)
    cleaned_tokens = []
    for lemma in lemmata:
        cleaned_tokens.append(lemma)

    return cleaned_tokens
