import sqlite3
import os
from flask import Flask, render_template, request

# конфигурация
DATABASE = '/tmp/flsite.db'
DEBUG = True
SECRET_KEY = 'rgoerkgpo324@#$@2544,wrrtwv0495'

app = Flask(__name__)
app.config.from_object(__name__)

app.config.update(dict(DATABASE=os.path.join(app.root_path, 'flsite.db')))


# if __name__ == '__main__':
#     app.run(debug=True)
