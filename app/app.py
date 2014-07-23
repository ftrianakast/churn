#!./../bin/python
from flask import Flask, request
from services import decode_data_package

app = Flask(__name__)


@app.route('/', methods=['POST'])
def calculateChurn():
    data_package = decode_data_package(request.json)
    print(data_package.resources)
    return "Calculating churn"

if __name__ == '__main__':
    app.run(debug=True)