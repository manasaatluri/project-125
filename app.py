from flask import Flask, jsonify, request
from classifier import  get_prediction

app = Flask(__name__)

@app.route("/predict-digit")
def predict_data():
  # image = cv2.imdecode(np.fromstring(request.files.get("digit").read(), np.uint8), cv2.IMREAD_UNCHANGED)
  image = "digit3.jpeg"
  prediction = get_prediction(image)
  return jsonify({
    "prediction": prediction
  }), 200

if __name__ == "__main__":
  app.run(debug=True)
