from flask import Flask, render_template,redirect, url_for, request, session
from bson import ObjectId
from datetime import datetime
import hashlib
import time
import mysql.connector


app = Flask(__name__)
app.config['SECRET_KEY'] = 'januar2020'
mydb = mysql.connector.connect(
	host="localhost",
	user="root",
	password="",
	database="domaci"
    )
@app.route('/')
@app.route('/index')
def index():
	return render_template('index.html')

@app.route('/raspored')
def raspored():
	mc = mydb.cursor()
	mc.execute("SELECT * FROM raspored")
	raspored = mc.fetchall()

	profesori = []
	ucionice = []
	for n in raspored:
		if n[3] not in profesori:
			profesori.append(n[3])

	for n in raspored:
		if n [7] not in ucionice:
			ucionice.append(n[7])
	return render_template("tabela.html", raspored = raspored, profesori = profesori, ucionice = ucionice)


if __name__ == '__main__':
	app.run(debug=True)