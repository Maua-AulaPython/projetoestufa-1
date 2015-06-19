from flask import Flask, request, jsonify
from flask.ext.sqlalchemy import SQLAlchemy
import json

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///device.db'
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)

from devicemodel import *

@app.route('/')
def index():
	return "Device Moromi, Rodrigo e Gui"


@app.route('/lista', methods=['GET'])
def device_list():
	infos = []
	for i in Device.query.all():
		print i.name, i.med.temp, i.med.umi, i.med.lum, i.med.date
		infos.append({'id': i.id, 'Nome': i.name, 'Temperatura': i.med.temp, 'Umidade': i.med.umi, 'Luminosidade': i.med.lum, 'Data': i.med.date.isoformat()})

	return json.dumps(infos)


@app.route('/new', methods=['POST'])
def device_new():
	if not request.json:
		return jsonify({'status': False})

	p = request.get_json()
	a = Device()
	a.name = p['name']
	a.med.temp = p['temp']
	a.med.umi = p['umi']
	a.med.lum = p['lum']
	a.med.date = datetime.datetime.now()
	db.session.add(a)
	db.session.commit()

	return jsonify({'status:': True})


if __name__ == '__main__':
	app.run(debug=True)


