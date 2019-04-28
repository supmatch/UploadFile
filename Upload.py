from flask import Flask, jsonify
from werkzeug.utils import secure_filename
import os
import json

app = Flask(__name__)

@app.route('/api/v1/Upload/', methods = ['GET', 'POST'])
def upload():
	upload_path = '/opt/flask/upload/'
	if os.path.exists(upload_path) is False:
		os.makedirs(upload_path)
	if request.method == 'POST':
		try:
			file_obj = request.files['file']
			file_path = os.path.join(upload_path,secure_filename(file_obj.filename))
			file_obj.save(file_path)
			return jsonify({'status':200, "msg": "upload {} success".format(file_obj.filename)})
		except Exception as e:
			app.logger.error(e)
			return jsonify({'status':200, "msg": "upload {} success".format(file_obj.filename)})
	else:
		file_lists = os.listdir(upload_path)
		return jsonify({json.dumps(file_lists)})
if __name__ == "__main__":
	app.run(debug=True)
