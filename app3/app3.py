import requests
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api3')
def api3():
    # Call API 1
    response1 = requests.get('http://app1:8080/api1')

    # Call API 2
    response2 = requests.get('http://app2:8081/api2')

    return jsonify({
        'response_from_api1': response1.json(),
        'response_from_api2': response2.json()
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8082)
