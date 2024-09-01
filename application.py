from flask import Flask

app = Flask(__name__)
application = app

@app.route("/")
def index():
    return "Hello World!"

@app.route("/data")
def data():
    return {"data": "example"}

@app.route("/data", methods=["POST"])
def extract():

    output = []

    extract_data = data()['data']

    for i in extract_data:
        output.append(i)

    output.sort()

    extracted_data = {"word": output}
    return extracted_data

extract()