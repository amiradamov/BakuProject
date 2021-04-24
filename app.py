from flask import Flask, request, render_template
from example import example

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/az')
def index_az():
    return render_template("az.html")

@app.route('/resp', methods=['GET'])
def response():
    # fname = request.form.get("q")
    fname = request.args.get("q")
    ex1 = example(fname)
    # return render_template('index.html', message = ex1)
    return ex1

if __name__ == "__main__":
    app.run(debug=True)


# @app.route('/response', methods=['POST'])
# def response():
    
#     fname = request.form.get("amir")
#     fname2 = example(fname)
#     note = request.form.get("note")
#     return render_template("index.html", name=fname2, note=note)