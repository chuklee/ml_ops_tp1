from flask import Flask, request, jsonify
from model_utils import get_model, get_tokenizer, get_prediction
app = Flask(__name__)

model = get_model()
tokenizer = get_tokenizer()

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json
    text = data["text"]
    prediction = get_prediction(text, model, tokenizer)
    return jsonify(prediction)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=4872)
