import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from flask import Flask, request, jsonify
from flask_cors import CORS
from github_api import get_repository_data
from analyzer import calculate_health_score

app = Flask(__name__)
CORS(app)


@app.route("/")
def home():
    return "GitHub Repository Health Analyzer API is running!"


@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.get_json()

    repo_url = data.get("repo_url")

    if not repo_url:
        return jsonify({"error": "Repository URL is required"}), 400

    try:
        repo_data = get_repository_data(repo_url)
        score = calculate_health_score(repo_data)

        return jsonify({
            "repository": repo_data,
            "health_score": score
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 400


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 5000)),
        debug=False
    )
