from flask import Flask, request, render_template, redirect
import os

app = Flask(__name__)
app.config ['UPLOAD_FOLDER'] = 'uploads/'

if not os.path.exists('uploads'):
    os.makedirs('uploads')

@app.route('/')
def home():
    return render_template('upload.html')

ALLOWED_EXTENSIONS = {'txt', 'pdf'}

def allowed_file(filename):
    return '.' in filename and \
            filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return 'No file part'
    file = request.files['file']
    if file.filename == '':
        return 'No selected file'
    if not allowed_file(file.filename):
        return 'Invalid file type'
    file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
    return 'File uploaded successfully'

if __name__ == "__main__":
    app.run(debug=True)
