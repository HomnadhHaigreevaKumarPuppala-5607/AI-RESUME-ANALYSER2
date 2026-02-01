from flask import Flask
from flask_cors import CORS
from routes.analyze_routes import analyze_bp

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return "Backend is alive"

app.register_blueprint(analyze_bp, url_prefix="/api/analyze")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)


