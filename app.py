from flask import Flask, request, jsonify
from routes.prediction import predict_risk
from routes.alerts import send_alert

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    result = predict_risk(data)
    return jsonify(result)

@app.route('/alert', methods=['POST'])
def alert():
    data = request.json
    result = send_alert(data)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
