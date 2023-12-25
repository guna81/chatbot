from flask import Flask, request, jsonify
import json
from bot import chat

# from flask_cors import CORS

app = Flask(__name__)
# CORS(app)

@app.route("/", methods=["POST"])
def chatbot_api():
    try:
        # Get user message from the request body
        prompt = request.json["prompt"]
        multi_response = request.json["multi_response"]
        # Check for predefined responses
        responses = chat(prompt)
        
        result = responses if multi_response else responses[0]
        # Generate JSON response for the platform (replace with your platform's specific format)
        # data = json.dumps({"message": responses})
        return jsonify(result), 200
    except Exception as e:
        print("error", e)
        return jsonify({
            "error": True
        })
    

if __name__ == "__main__":
    app.run(
        host='0.0.0.0',
        port=5001,
        debug=True,
    )