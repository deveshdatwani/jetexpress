from flask import Flask, Blueprint

def create_app():

	app = Flask(__name__, instance_relative_config=True)

	@app.route('/', methods=['GET','POST'])
	def say_hi():

		return 'Hi'
	from . import auth
	app.register_blueprint(auth.bp)

	return app

