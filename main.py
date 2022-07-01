#!/usr/bin/env python3

import sys
import builtins
import flask
from flask import Flask, redirect, render_template, send_from_directory, jsonify, Response
from flask_swagger_ui import get_swaggerui_blueprint
from safrs import SAFRSBase, SAFRSAPI, jsonapi_rpc
from sqlalchemy.sql import select
from datetime import datetime


from config import *
from schema import *

Compress(app)

def formatDate(raw):
  raw_str=str(raw)
  if len(raw_str)!=8:
    return "????-??-??"
  return raw_str[0:4]+"-"+raw_str[4:6]+"-"+raw_str[6:8]

def getWeekDay(raw):
  raw_str=str(raw)
  if len(raw_str)!=8:
    return "???????"
  return datetime(int(raw_str[0:4]),int(raw_str[4:6]),int(raw_str[6:8]),0,0,0).strftime("%A")


@app.route("/")
def index():
  return render_template("index.html")
@app.route("/plan/<plan_id>")
def plan(plan_id):
  plan = Plan.query.filter(Plan.id==plan_id).first()
  if plan==None:
    return "not_found", 404
  return render_template("plan.html", formatDate=formatDate, getWeekDay=getWeekDay, plan_id=plan_id, plan_start=plan.start, plan_end=plan.end, plan_notes=plan.notes, plan_img=plan.img, person1=PERSON1, person2=PERSON2)

@app.route("/static/<path:path>")
def send_static(path):
  return send_from_directory("static", path)
@app.route("/scloud_assets/<path:path>")
def send_scloud_assets(path):
  return send_from_directory("scloud_assets", path)

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
