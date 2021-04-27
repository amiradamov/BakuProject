from flask import Flask, request, render_template
from example import example

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index1.html')

@app.route('/out', methods=['POST'])
def response():
    if (request.form.get("algorithms")=="lemmatizer"):
        fname = request.form.get("text")
        ex1 = "Hello, "+ fname
        return render_template('index1.html', message = ex1)
    else:
        return render_template('index1.html', message = "something went wrong")


if __name__ == '__main__':
    app.run(debug = True, port = 8080)