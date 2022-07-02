from config import *
from safrs import SAFRSBase


class Plan(SAFRSBase, db.Model):
  __tablename__ = "Plan"
  id          = db.Column(db.Integer, primary_key=True)
  entries     = db.relationship("Entry", back_populates="plan", lazy="select")

  img         = db.Column(db.String(256))
  start       = db.Column(db.Integer())
  end         = db.Column(db.Integer())

  notes       = db.Column(db.String(1024))


class Entry(SAFRSBase, db.Model):
  __tablename__ = "Entry"
  id          = db.Column(db.Integer, primary_key=True)
  date        = db.Column(db.Integer())
  plan_id     = db.Column(db.Integer, db.ForeignKey("Plan.id"))
  plan        = db.relationship("Plan", back_populates="entries")

  person1     = db.Column(db.String(512))
  person1_url = db.Column(db.String(1024))
  person2     = db.Column(db.String(512))
  person2_url = db.Column(db.String(1024))
  together    = db.Column(db.Boolean())
