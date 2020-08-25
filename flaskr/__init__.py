from flask import Flask, Blueprint, render_template

def create_app():

	app = Flask(__name__, instance_relative_config=True)

	@app.route('/', methods=['GET','POST'])
	def say_hi():

		return render_template('login.html')

	from . import auth
	app.register_blueprint(auth.bp)

	return app

