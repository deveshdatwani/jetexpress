from flask import Flask, Blueprint, request, render_template

bp = Blueprint('auth', __name__)

@bp.route('/auth', methods = ['GET', 'POST'])
def authenticate():

	if request.method == 'POST':
		username = request.form['username']
		password = request.form['password']

	elif request.method == 'GET':
		colors = ['devesh', 'datwani']
		response = render_template('auth.html', colors=colors)

	return response