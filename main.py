#!/usr/bin/env python3

import sys
import builtins
import flask
from flask import Flask, redirect, render_template, send_from_directory, jsonify, Response
from flask_swagger_ui import get_swaggerui_blueprint
from safrs import SAFRSBase, SAFRSAPI, jsonapi_rpc
from sqlalchemy.sql import select

from config import *
from schema import *

Compress(app)

@app.route("/")
def index():
  return render_template("index.html")

@app.route("/static/<path:path>")
def send_static(path):
  return send_from_directory("static", path)
@app.route("/fonts/<path:path>")
def send_fonts(path):
  return send_from_directory("fonts", path)

if __name__ == "__main__":
  HOST = sys.argv[1] if len(sys.argv) == 3 else "localhost"
  PORT = int(sys.argv[2]) if len(sys.argv) == 3 else 5555
  db.init_app(app)
  db.app = app
  db.create_all()
  API_PREFIX = "/api"

  with app.app_context():
    api = SAFRSAPI(app, host="{}".format(HOST), port=PORT, prefix=API_PREFIX)
    api.expose_object(Plan)
    api.expose_object(Entry)

    app.run(host=HOST, port=PORT)
