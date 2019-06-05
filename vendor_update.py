from flask import Flask, request, render_template, redirect, g
import os

app = Flask(__name__)

app.config.from_object(__name__)

app.config.update(
    DATABASE=os.path.join(app.root_path, 'vendor_updates.db'),
    SECRET_KEY=b'4\x81\xc4\x8a\x0f\xcc\xaa\x17Q\xde\x93\x9d',
    USERNAME='admin',
    PASSWORD='default'
)

@app.route('/', methods=["GET", "POST"])
def updates_upload():
    if request.method == 'POST':
        if 'updates_file' not in request.files:
            return redirect(request.url)
        updates_file = request.files['updates_file']
        if updates_file:
            contents = updates_file.read()
            process_vendor_updates(contents)
            return render_template('success.html')
    else:
        return render_template('file_upload.html')
