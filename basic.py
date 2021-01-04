from flask import Flask, jsonify
import requests
from flask_cors import CORS
app = Flask(__name__)
CORS(app)

@app.route('/country/<string:name>', methods=['GET'])
def get_tasks(name):

    url = "https://covid-19-data.p.rapidapi.com/country"

    querystring = {"name": name}

    headers = {
        'x-rapidapi-key': "1571af62a8mshe4fd36bf739725dp1f6f35jsn66537391a214",
        'x-rapidapi-host': "covid-19-data.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    return jsonify(response.json()[0])



if __name__ == '__main__':
    app.run(debug=True)