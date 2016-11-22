import time
import datetime
import sys
import Adafruit_DHT
import sqlite3
from flask import Flask, request, render_template

app = Flask(__name__)
app.debug = True

@app.route("/real_time_temp")
def display():
	humidity_read, temperature_read = Adafruit_DHT.read_retry(Adafruit_DHT.AM2302, 22)
	
	conn=sqlite3.connect('/var/temperature_logger/temp_data.db')
	curs=conn.cursor()
	curs.execute("SELECT * FROM temperatures")
	temperatures = curs.fetchall()
	curs.execute("SELECT * FROM humidities")
	humidities = curs.fetchall()
	conn.close()
	
	if humidity_read is not None and temperature_read is not None:
		return render_template("index.html",temp=temperature_read,hum=humidity_read, temp_arr=temperatures,hum_arr=humidities)
	else:
		return render_template("error.html")


if __name__ == "__main__":
	app.run(host='0.0.0.0', port=8080)
