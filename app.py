from flask import Flask, request, jsonify, redirect, send_from_directory
import os

app = Flask(__name__)

@app.route("/")
def hello():
    return "<h1>Привет!</h1>"

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        if file:
            #filename = secure_filename(file.filename)
            file.save(os.path.join("storage", file.filename))
            return redirect("list")
    return '''
        <!doctype html>
            <title>Загрузка файла</title>
            <h1>Загрузка файла</h1>
            <form action="" method=post enctype=multipart/form-data>
                <p><input type=file name=file>
                <input type=submit value=Upload>
            </form>
        </html>
    '''

@app.route("/list")
def list():
    files = os.listdir("storage")
    return jsonify(files)

@app.route("/files/<filename>")
def download(filename):
    return send_from_directory("storage", filename, as_attachment=True)