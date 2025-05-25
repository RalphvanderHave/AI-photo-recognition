from flask import Flask, request, jsonify
import os
from werkzeug.utils import secure_filename
from predict import predict_single_image
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    if file:
        filename = secure_filename(file.filename)
        save_path = os.path.join(UPLOAD_FOLDER, filename)
        file.save(save_path)

        # Predict using the saved image
        predicted_labels = predict_single_image(save_path)

        return jsonify({'predicted_labels': predicted_labels}), 200


if __name__ == '__main__':
    app.run(debug=True)