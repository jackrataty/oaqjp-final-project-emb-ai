from flask import Flask, jsonify, request
import json

app = Flask(__name__)

with open("sample_response.json", "r") as f:
    SAMPLE = json.load(f)

@app.post("/")
def emotion_predict():
    # optional: inspect what your client sends
    # print(request.get_json(silent=True))
    print(request.headers.get("grpc-metadata-mm-model-id"))
    return jsonify(SAMPLE)




if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5001, debug=True)
