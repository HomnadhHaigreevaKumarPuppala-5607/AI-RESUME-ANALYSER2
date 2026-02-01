from flask import Blueprint, request, jsonify
from utils.resume_analyzer import analyze_resume

analyze_bp = Blueprint("analyze", __name__)

@analyze_bp.route("/", methods=["POST"])
def analyze():
    data = request.get_json()
    resume_text = data.get("resume", "")
    job = data.get("job", "")

    result = analyze_resume(resume_text, job)
    return jsonify(result)
