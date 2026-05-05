from flask import Flask, request, jsonify
from flask_cors import CORS
from firebase_config import db
from anonymizer import anonymize

app = Flask(__name__)
CORS(app)

# 📡 Upload data
@app.route('/upload', methods=['POST'])
def upload():
    try:
        data = request.json
        db.collection("health_data").add(data)
        return jsonify({"status": "stored"})
    except Exception as e:
        print("UPLOAD ERROR:", e)
        return jsonify({"error": str(e)}), 500


# 🔐 Get data (Doctor & Coach)
@app.route('/get_data', methods=['GET'])
def get_data():
    try:
        role = request.headers.get("role")

        docs = db.collection("health_data").stream()
        result = []

        for doc in docs:
            data = doc.to_dict()

            if role == "doctor":
                result.append({
                    "player_id": data.get("player_id", "unknown"),
                    "heart_rate": data.get("heart_rate", 0),
                    "temperature": data.get("temperature", 0),
                    "timestamp": data.get("timestamp", "N/A")
                })

            elif role == "coach":
                heart = data.get("heart_rate", 0)
                player = data.get("player_id", "unknown")

                fatigue = int((heart / 180) * 10)

                result.append({
                    "player_id": player,
                    "fatigue": fatigue
                })

        return jsonify(result)

    except Exception as e:
        print("GET_DATA ERROR:", e)
        return jsonify({"error": str(e)}), 500


# 🔒 Analytics
@app.route('/analytics', methods=['GET'])
def analytics():
    try:
        docs = db.collection("health_data").stream()
        result = []

        for doc in docs:
            data = doc.to_dict()
            result.append(anonymize(data))

        return jsonify(result)

    except Exception as e:
        print("ANALYTICS ERROR:", e)
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)