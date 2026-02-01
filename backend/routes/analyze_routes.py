from flask import Blueprint, request, jsonify
from utils.resume_analyzer import analyze_resume

analyze_bp = Blueprint("analyze", __name__)

@analyze_bp.route("/analyze", methods=["POST"])
def analyze():
    data = request.get_json()
    resume = data.get("resume", "")
    job = data.get("job", "")

    result = analyze_resume(resume, job)
    return jsonify(result)


