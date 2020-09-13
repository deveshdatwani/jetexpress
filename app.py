from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
	return render_template("index.html")

@app.route('/aboutus')
def about():
	print('Hi')
	return render_template('about.html')
