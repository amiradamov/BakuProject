from flask import Flask, request, render_template
from example import example
from naive_bayes_test import NBC
from svm_classifier_test import SVMC
from rnn_classifier_test import RNNC
from random_forest_classifier_test import RFC
from aznlp.azerbaijani_lemmatizer import AzerbaijaniLemmatizer
from text_classification.sentence_cleaner import *
from collections import Counter

nbc = NBC()
print('set up NB classifier')
svmc = SVMC()
print('set up SVM classifier')
rnnc = RNNC()
print('set up RNN classifier')
rfc = RFC()
print('set up RF classifier')
azl = AzerbaijaniLemmatizer()
print('set up Lemmatizer')

def most_frequent(List):
    occurence_count = Counter(List)
    return occurence_count.most_common(1)[0][0]

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/az')
def index_az():
    return render_template("az.html")

@app.route('/resp', methods=['POST'])
def response():

    outText = ""
    inText = request.args.get("q")
    lematizer = request.args.get("lem")
    classifier = request.args.get("class")

    if (lematizer == 'true'):
        print('LEMMATIZE')
        words = [word for word in inText.split()]
        print(words)
        words = clean_tokens_stopwords(words)
        outText = ' '.join(azl.lemmatize(words))
        print(outText)
        #print('here')
        return outText
    
    else:
        arr = []
        nb_out = nbc.test(inText)
        rnn_out = rnnc.test(inText)
        svmc_out = svmc.test(inText)
        arr.append(nb_out)
        arr.append(rnn_out)
        arr.append(svmc_out)
        outText = most_frequent(arr)
        return outText

    # elif (classifier == "naive_bayes"):
    #     print('NB')
    #     outText = nbc.test(inText)
    #     print(outText)
    #     return outText
        
    # elif (classifier == "neural_networks"):
    #     print('RNN')
    #     outText = rnnc.test(inText)
    #     print(outText)
    #     return outText

    # elif (classifier == "random_forest"):
    #     print('RF')
    #     outText = "random_forest " + inText
    #     print(outText)
    #     return outText

    # elif (classifier == "support_vector_machine"):
    #     print('SVM')
    #     outText = svmc.test(inText)
    #     print(outText)
    #     return outText
    

if __name__ == "__main__":
    app.run(debug=True)


# @app.route('/response', methods=['POST'])
# def response():
    
#     fname = request.form.get("amir")
#     fname2 = example(fname)
#     note = request.form.get("note")
#     return render_template("index.html", name=fname2, note=note)