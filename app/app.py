# from flask import Flask, request, jsonify, redirect, send_file
# import os
# from datetime import datetime
# import json

# app = Flask(__name__)

# os.makedirs("storage", exist_ok=True)

# def today_dir():
#     folder = datetime.now().strftime("%d-%m-%Y")
#     path = os.path.join("storage", folder)
#     os.makedirs(path, exist_ok=True)
#     return path

# @app.route("/")
# def hello():
#     return '''
#             <h1>Привет!</h1>
#             <a href="upload">Загрузить файл</a>
#         '''

# @app.route("/upload", methods=["GET", "POST"])
# def upload_file():
#     if request.method == "POST":
#         file = request.files["file"]
#         if file:
#             #filename = secure_filename(file.filename)
#             folder = today_dir()
#             file_path = os.path.join(folder, file.filename)
#             file.save(file_path)

#             metadata = {
#                 "upload_date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
#                 "size": os.path.getsize(file_path)
#             }

#             with open(file_path + ".meta.json", "w") as f:
#                 json.dump(metadata, f)

#             return redirect("/list")
#     return '''
#         <!doctype html>
#             <title>Загрузка файла</title>
#             <h1>Загрузка файла</h1>
#             <form action="" method=post enctype=multipart/form-data>
#                 <input type=file name=file>
#                 <input type=submit value=Загрузить>
#             </form>
#         </html>
#     '''

# @app.route("/list")
# def list():
#     files = []
#     for root, _, filenames in os.walk("storage"):
#         for filename in filenames:
#             if not filename.endswith('.meta.json'):
#                 file_path = os.path.join(root, filename)
#                 meta_path = file_path + ".meta.json"

#                 metadata = {}
#                 if os.path.exists(meta_path):
#                     with open(meta_path) as f:
#                         metadata = json.load(f)

#                 files.append({
#                     "path": os.path.relpath(file_path, "storage"),
#                     **metadata
#                 })
    
#     return jsonify(files)

# @app.route("/files/<path:filepath>")
# def download(filepath):
#     full_path = os.path.join("storage", filepath)
#     return send_file(full_path, as_attachment=True)

# if __name__ == "__main__":
#     app.run(host="0.0.0.0", port=8000)

from flask import Flask
import psycopg2
import os

app = Flask(__name__)

DB_HOST = os.getenv("DB_HOST")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")


@app.route("/")
def index():
    try:
        conn = psycopg2.connect(
            host=DB_HOST,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD
        )
        conn.close()
        return "Connected to DB container!"
    except Exception as e:
        return f"DB connection failed: {e}"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
