# Secure File Sharing System

This project is a simple secure file sharing system built using Python and Flask. It allows users to upload files, which are encrypted before storage and decrypted during download.

## Features
- File upload and download functionality
- Encryption of files before storage
- Decryption of files during download
- Simulates secure client-server file transfer

## Tech Stack
- Python
- Flask
- Cryptography (Fernet)

## How it Works
1. User uploads a file through the web interface
2. The file is encrypted and stored on the server
3. When the file is requested, it is decrypted and downloaded

## Setup
Install dependencies:
pip install flask cryptography

Run the app:
python app.py

Open in browser:
http://127.0.0.1:5000
