from aznlp.suffixes import inflectional_dict, inflectional
from aznlp.words import luget, stopwords


class AzerbaijaniLemmatizer:

    def __init__(self):
        self.lemmata = []
        self.words = luget
        self.stop_words = stopwords

    def lemmatize(self, words):
        list_of_lemma = []
        for word in words:
            self.lemmata = []
            self.lemmatize_single_word(word)
            self.lemmata.sort(key=len)
            list_of_lemma.append(self.lemmata[0] if self.lemmata and len(self.lemmata) > 0 else word)
        return list_of_lemma

    def lemmatize_single_word(self, word):
        # fix ending of the word
        word = self.fix_word_ending(word)

        # if word is a numeric expression return it
        if word.isnumeric():
            self.lemmata.append(word)
            return self.lemmata

        if word.endswith('lar') or word.endswith('lər') or word.endswith('maq') \
                or word.endswith('mək') and word[:-3] in self.words:
            self.lemmata.append(word[:-3])
            return self.lemmata

        elif word in self.words:
            if word.endswith('lar') or word.endswith('lər') or word.endswith('maq') \
                    or word.endswith('mək') and word[:-3] in self.words:
                word = word[:-3]
            self.lemmata.append(word)
            return self.lemmata
        # check for suffixes in a word
        for suffix in inflectional:
            if word.endswith(suffix) and suffix in inflectional_dict['İstisna leksik şəkilçilər']:
                self.lemmata.append(word)
                return self.lemmata
            if word.endswith(suffix):
                self.lemmatize_single_word(word[:word.rfind(suffix)])

    # fix words with certain endings
    def fix_word_ending(self, word):
        if word.endswith('ığ') or word.endswith('üğ') or word.endswith('uğ') or word.endswith('iğ') \
                or word.endswith('ağ'):
            word_as_list = list(word)
            word_as_list[-1] = 'q'
            return ''.join(word_as_list)
        if word.endswith('iy') or word.endswith('üy') or word.endswith('əy') or word.endswith('liy') \
                or word.endswith('lüy'):
            word_as_list = list(word)
            word_as_list[-1] = 'k'
            return ''.join(word_as_list)
        if word == 'ged':
            word = 'get'
            return word
        if word == 'ed':
            word = 'et'
            return word
        return word
