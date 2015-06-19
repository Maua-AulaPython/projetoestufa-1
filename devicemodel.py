from deviceserver import db
from flask import Flask, request, jsonify
from flask.ext.sqlalchemy import SQLAlchemy
import json
import datetime

class Device(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(80))
	med =db.relationship('Measure')

class Measure(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        device_id = db.Column(db.Integer, db.ForeignKey('device.id'))
        temp = db.Column(db.Integer)
	umi = db.Column(db.Integer)
	lum = db.Column(db.Integer)
	date = db.Column(db.DateTime)
