from flask import Flask
import os

app = Flask(__name__)

app.config.from_object(__name__)

app.config.update(
    DATABASE=os.path.join(app.root_path, 'vendor_updates.db'),
    SECRET_KEY=b'4\x81\xc4\x8a\x0f\xcc\xaa\x17Q\xde\x93\x9d',
    USERNAME='admin',
    PASSWORD='default'
)

@app.route('/')
def hello_world():
    return 'Hello, World!'
