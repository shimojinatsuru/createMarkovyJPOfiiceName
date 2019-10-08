from flask import Flask, render_template, request

import os
import json
import markovify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('main.html')

@app.route('/generate', methods=['GET'])
def main():
    with open('model.json','r') as f:
        model_json = json.load(f)

    reconstituted_model = markovify.Text.from_json(model_json)

    office_name = []
    for _ in range(10):
        predicted_name = reconstituted_model.make_sentence()
        if predicted_name == None:
            pass
        else:
            office_name.append(''.join(predicted_name.split()))

    return render_template('main.html',office_name=office_name)

if __name__ == "__main__":
    # Herokuからポート番号を取得するようにする。
    # Get the port number from Heroku.
    port = int(os.getenv("PORT"))
    app.run(host='0.0.0.0', port=port, debug=True)