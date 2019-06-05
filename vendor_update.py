from flask import Flask, request, render_template, redirect, g
from sqlite3 import dbapi2 as sqlite3 
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


def connect_db():
    rv = sqlite3.connect(app.config['DATABASE'])
    rv.row_factory = sqlite3.Row
    return rv

def get_db():
    if not hasattr(g, 'sqlite_db'):
        g.sqlite_db = connect_db()
    return g.sqlite_db

def init_db():
    db = get_db()
    with app.open_resource('schema.sql', mode='r') as f:
        db.cursor().executescript(f.read())
    db.commit()


def process_vendor_updates(update_str):
    pass
