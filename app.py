from flask import Flask, request, render_template
from example import example

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
        outText = "LEMATIZER " + inText

    elif (classifier == "naive_bayes"):
        outText = "naive_bayes " + inText

    elif (classifier == "neural_networks"):
        outText = "neural_networks " + inText

    elif (classifier == "random_forest"):
        outText = "random_forest " + inText

    elif (classifier == "support_vector_machine"):
        outText = "support_vector_machine " + inText
    return outText

if __name__ == "__main__":
    app.run(debug=True)


# @app.route('/response', methods=['POST'])
# def response():
    
#     fname = request.form.get("amir")
#     fname2 = example(fname)
#     note = request.form.get("note")
#     return render_template("index.html", name=fname2, note=note)