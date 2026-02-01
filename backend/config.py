import os

class Config:
    # Secret key (used later if you add sessions / auth)
    SECRET_KEY = "resume-analyzer-secret-key"

    # Upload folder path
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    UPLOAD_FOLDER = os.path.join(BASE_DIR, "uploads")

    # Allowed resume file types
    ALLOWED_EXTENSIONS = {"txt"}

    # Max file size (2MB)
    MAX_CONTENT_LENGTH = 2 * 1024 * 1024

    # Debug mode
    DEBUG = True
