from flask import Flask, request

app = Flask(__name__)
application = app


@app.route("/")
def index():
    return "Hello World!"

@app.route("/data", methods=["POST"])
def extract():

    output = []   

    extract_data = {"data": request.json["data"]}

    for i in extract_data["data"]:
        output.append(i)

    output.sort()

    extracted_data = {"word": output}

    return extracted_data

if __name__ == "__main__":
    app.run(debug=True)