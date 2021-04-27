from text_classification.sentence_cleaner import *
from config import ROOT_DIR
import pickle

class RFC:

    def __init__(self):
        self.vectorizer_file = open(ROOT_DIR + '/text_classification/pickles/trainingdata_vect_RF.pickle', 'rb')
        self.rf_file = open(ROOT_DIR + '/text_classification/pickles/trainingdata_model_RF.pickle', 'rb')
        self.Tfidf_vect = pickle.load(self.vectorizer_file, encoding='utf-8')
        self.rf_classifier = pickle.load(self.rf_file, encoding='utf-8')

    def start(self, sentence):
        
        words = [w for w in sentence.split()]
        custom_tokens = clean_tokens(words)
        custom_sentence = ' '.join(custom_tokens)
        vect = self.Tfidf_vect.transform([custom_sentence])
        prediction = self.rf_classifier.predict(vect)

        if prediction == 0:
            return 'Arxitektura'
        elif prediction == 1:
            return 'Din'
        elif prediction == 2:
            return 'Edebiyyat'
        elif prediction == 3:
            return 'Ekologiya'
        elif prediction == 4:
            return 'Elm'
        elif prediction == 5:
            return 'Felsefe'
        elif prediction == 6:
            return 'Herb'
        elif prediction == 7:
            return 'Huquq'
        elif prediction == 8:
            return 'Idman'
        elif prediction == 9:
            return 'Incesenet'
        elif prediction == 10:
            return 'Jurnalistika'
        elif prediction == 11:
            return 'Kend Teserrufati'
        elif prediction == 12:
            return 'Maliyye'
        elif prediction == 13:
            return 'Medeniyyet'
        elif prediction == 14:
            return 'Proqramlashdirma'
        elif prediction == 15:
            return 'Psixologiya'
        elif prediction == 16:
            return 'Rabite'
        elif prediction == 17:
            return 'Siyaset'
        elif prediction == 18:
            return 'Sosiologiya'
        elif prediction == 19:
            return 'Tarix'
        elif prediction == 20:
            return 'Tibb'
        elif prediction == 21:
            return 'Turizm'


        self.vectorizer_file.close()
        self.rf_file.close()
