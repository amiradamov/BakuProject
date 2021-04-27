# # It can be used to reconstruct the model identically.
# reconstructed_model = keras.models.load_model("my_model")
#
# Let's check:
import csv
import tensorflow as tf
import numpy as np
from text_classification.sentence_cleaner import clean_tokens
from tensorflow.keras.preprocessing.text import Tokenizer
import keras
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Flatten, LSTM, Dropout, Activation, Embedding, Bidirectional

vocab_size = 5000  # make the top list of words (common words)
embedding_dim = 64
max_length = 200
trunc_type = 'post'
padding_type = 'post'
oov_tok = '<OOV>'  # OOV = Out of Vocabulary
training_portion = .8
import pickle
from config import ROOT_DIR


class RNNC:
    
    def __init__(self):
        with open(ROOT_DIR + "/text_classification/pickles/rnn_tokenizer.pickle", 'rb') as handle:
            self.tokenizer = pickle.load(handle)
        self.model = keras.models.load_model(ROOT_DIR + "/text_classification/pickles/rnn_model")

    def test(self, txt):
        print(txt)
        print('-------------------------------')
        txt = ''.join(txt)
        print(txt)
        words = [w for w in txt.split()]
        txt = clean_tokens(words)
        print(txt)
        txt = [' '.join(txt)]
        print(txt)

        seq = self.tokenizer.texts_to_sequences(txt)
        print(seq)
        padded = pad_sequences(seq, maxlen=max_length)

        pred = self.model.predict(padded)
        labels = ['arxitektura', 'din', 'edebiyyat', 'ekologiya', 'elm', 'felsefe', 'herb', 'huquq', 'idman',
                  'incesenet', 'jurnalistika', 'kendteserrufati', 'maliyye', 'medeniyyet', 'proqramlaşdırma',
                   'psixologiya', 'rabiteveinformatika', 'siyaset', 'sosiologiya', 'tarix', 'tibb', 'turizm']

        print(pred)
        print(np.argmax(pred))
        tosubtract = 0
        if np.argmax(pred) == 22:
            tosubtract = 1
        return labels[np.argmax(pred) - tosubtract]
