import flask
import logging
from logging.handlers import RotatingFileHandler
from flask import request, jsonify
from datetime import datetime
app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods=['GET'])
def index():
	return '<h1>Model server running.</h1>'

@app.route('/save_data', methods=['POST'])
def save():
	app.logger.info("save API called.")

	if request.mimetype == 'application/json':
		input_json = request.get_json(force=True)
	else:
		input_json = request.form.to_dict()

	# input_json = flask.request.get_json(force=True)
	
	app.logger.info("API Request => " + str(input_json))
	


	app.logger.info("API Response => \n" + str(res))
	app.logger.info("changeset API finished.")
	return jsonify(res)

@app.route('/get_data', methods=['GET'])
def data():
	app.logger.info("date API started.")

	if request.mimetype == 'application/json':
		input_json = request.get_json(force=True)
	else:
		input_json = request.form.to_dict()

	# input_json = flask.request.get_json(force=True)
	
	app.logger.info("API Request => " + str(input_json))
	

	app.logger.info("API Response => " + str(all_res))
	app.logger.info("date API finished.")
	return jsonify(all_res)

if __name__=='__main__':
	rotating_file_handler = RotatingFileHandler('main.log', maxBytes=1024*1024*100, backupCount=1)
	log_formatter = logging.Formatter("[%(asctime)s]\t%(levelname)s\t%(module)s\t%(message)s")
	rotating_file_handler.setFormatter(log_formatter)
	rotating_file_handler.setLevel(logging.INFO)
	app.logger.setLevel(logging.INFO)
	app.logger.addHandler(rotating_file_handler)
	app.run()
