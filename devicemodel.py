from deviceserver import db
import datetime

class Device(db.Model):
	id		= db.Column(db.Integer, primary_key=True)
	temp	= db.Column(db.Integer)
	umi	= db.Column(db.Integer)
	lum     = db.Column(db.Integer)
	date    = db.Column(db.DateTime)