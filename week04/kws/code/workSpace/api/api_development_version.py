from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from datetime import *
import os, psycopg2, json


#Init app
app = Flask(__name__)
connection, cursor = 0, 0

with open('config.json') as config_file:
	config = json.load(config_file)

def db_connect():
	try:
	    connection = psycopg2.connect(user = config.get('DBUSER'),
	                                  password = config.get('DBPASS'),
	                                  host = config.get('DBHOST'),
	                                  port = config.get('DBPORT'),
	                                  database = config.get('DBNAME'))
	    cursor = connection.cursor()
	    # print ( connection.get_dsn_parameters(),"\n")
	    return connection, cursor
	except (Exception, psycopg2.Error) as error :
	    return False

def db_close(connection, cursor):
	if(connection):
		cursor.close()
		connection.close()
		print("PostgreSQL connection is closed")


@app.route('/gets/weather/v0.1/historical', methods = ['GET'])
def get_historical():
	""" Give the historical weather data in between the given date """
	if len(request.args) > 0:
		res_json = dict()
		try:
			from_date = request.args['from_date']
			to_date = request.args['to_date']

			select_query = "select * from weather_station where \"datetime\" >= '" + from_date + "' and \"datetime\" <= '" + to_date + "'"
			cursor.execute(select_query)
			res = cursor.fetchall()

			for row in res:
				datetime, temperature, humidity, rstatus, rlevel, location = str(row[1]), row[2], row[3], row[4], row[5], row[6]
				res_json[datetime] = { "temperature" : temperature,
										"humidity" : humidity,
										"rstatus" : rstatus,
										"rlevel" : rlevel,
										"location" : location
				}
			return jsonify(res_json)
		except Exception as e:
			print(e)
			return jsonify({ "code" : 400})

	return jsonify({ "code" : 200})

@app.route('/gets/weather/v0.1/lastest', methods = ['GET'])
def get_lastest():
	""" Give the lastes weather data limited with the given amount """
	if len(request.args) > 0:
		res_json = dict()
		try:
			count = request.args['count']

			select_query = "select * from weather_station order by id desc limit " + count
			cursor.execute(select_query)
			res = cursor.fetchall()

			for row in res:
				datetime, temperature, humidity, rstatus, rlevel, location = str(row[1]), row[2], row[3], row[4], row[5], row[6]
				res_json[datetime] = { "temperature" : temperature,
										"humidity" : humidity,
										"rstatus" : rstatus,
										"rlevel" : rlevel,
										"location" : location
				}
			return jsonify(res_json)
		except Exception as e:
			print(e)
			return jsonify({ "code" : 400})

	return jsonify({ "code" : 200})


@app.route('/gets/v0.1/current_datetime', methods = ['GET'])
def current_datetime():
	current_datetime = datetime.now()
	str_current_datetimestamp = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
	return str_current_datetimestamp

#Run server
if __name__ == '__main__':
	app.debug = False
	connection, cursor = db_connect()
	host = os.environ.get('IP', '0.0.0.0')
	port = int(os.environ.get('PORT', 8019))
	app.run(host=host, port=port)
