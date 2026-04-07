# app.py

from flask import Flask, render_template, request, send_file
import os
from crypto_utils import encrypt_file, decrypt_file

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/upload", methods=["POST"])
def upload():
    file = request.files["file"]
    file_data = file.read()

    encrypted_data = encrypt_file(file_data)

    file_path = os.path.join(UPLOAD_FOLDER, file.filename)

    with open(file_path, "wb") as f:
        f.write(encrypted_data)

    return "File uploaded and encrypted successfully!"

@app.route("/download/<filename>")
def download(filename):
    file_path = os.path.join(UPLOAD_FOLDER, filename)

    with open(file_path, "rb") as f:
        encrypted_data = f.read()

    decrypted_data = decrypt_file(encrypted_data)

    temp_path = os.path.join(UPLOAD_FOLDER, "temp_" + filename)

    with open(temp_path, "wb") as f:
        f.write(decrypted_data)

    return send_file(temp_path, as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)
