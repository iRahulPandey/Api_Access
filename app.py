# import libraries
from flask import Flask, request, jsonify, render_template
import traceback
import requests
import json


# Your API definition
app = Flask(__name__)


@app.route("/")
def home():
    # return "Hello, Flask!"
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict_html():
    if url:
        try:
            # input data
            input_data = [request.form.to_dict()]
            for dicts in input_data:
                for keys in dicts:
                    dicts[keys] = int(dicts[keys])
                    
            # update key to uppercase
            input_data_new = {k.upper():input_data[0][k] for k in input_data[0].keys()}

            # data to be sent to the model
            data = json.dumps(input_data_new)
            
            # to the api
            prediction = requests.post(url, data).json()['prediction']
            output = round(prediction[0], 2)

            return render_template(
                "index.html", prediction_text="Prediction {}".format(output)
            )

        except:

            return jsonify({"trace": traceback.format_exc()})
        
if __name__ == "__main__":

    port = 9696  # If you don't provide any port the port will be set to 12345
    url = 'https://bostonappfastapi.herokuapp.com/predict'  # Url of the API --> model hosted on Heroku
    # app.run(debug=True)
    # app.run(port=port, debug=True, host="0.0.0.0")
    # on container
    app.run(debug=True, host="0.0.0.0")
    # on local
    # app.run(debug=True, host="127.0.0.1")