import yaml

file = open(r'./config.yml')
cfg = yaml.full_load(file)

DB_URI         = cfg['DB']
DEBUG_ENABLED  = cfg['Debug']

from flask import Flask
from flask_caching import Cache
from flask_compress import Compress
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.debug=DEBUG_ENABLED
app.secret_key = 'development'
cache = Cache(app, config={"CACHE_TYPE": "simple"})
app.config["DEBUG"] = DEBUG_ENABLED
app.config["SQLALCHEMY_DATABASE_URI"] = DB_URI
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
app.config["PYRAMID_PREVENT_CACHEBUST"] = True
COMPRESS_MIMETYPES = ['text/html', 'text/css', 'text/xml', 'application/json', 'application/javascript']
COMPRESS_LEVEL = 6
COMPRESS_MIN_SIZE = 500

db = SQLAlchemy()