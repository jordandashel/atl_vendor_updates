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
            updates_file_contents = updates_file.read().decode('utf-8')
            parse_file_contents(updates_file_contents)
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


def parse_file_contents(update_items):
    records = update_items.split('\n')
    processed_records = [parse_record_data(record)
            for record in records if record]
    return processed_records

def parse_record_data(record):
    fields = record.split('\t')
    record = {}
    record['id'] = fields[0]
    record['first_name'] = fields[1]
    record['last_name'] = fields[2]
    record['street_address'] = fields[3]
    record['state'] = fields[4]
    record['zip_code'] = fields[5]
    record['purchase_status'] = fields[6]
    record['product_id'] = fields[7]
    record['product_name'] = fields[8]
    record['item_price'] = fields[9]
    record['date_time'] = fields[10]

    return record
