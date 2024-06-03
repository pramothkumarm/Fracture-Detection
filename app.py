from flask import Flask, request, render_template, send_from_directory, jsonify
import os
from ultralytics import YOLO

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
RESULT_FOLDER = 'results'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(RESULT_FOLDER, exist_ok=True)

# Load the YOLO model
model = YOLO(r'B:\Project\Bone Fracture\best.pt')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({"message": "No file part"}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({"message": "No selected file"}), 400
    if file:
        filepath = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(filepath)
        
        # Run YOLO prediction
        results = model.predict(source=filepath, conf=0.25)
        
        # Process the results
        if len(results[0].boxes) == 0:
            return jsonify({"message": "not fractured"})
        else:
            annotated_image_path = os.path.join(RESULT_FOLDER, file.filename)
            results[0].plot(save=True, filename=annotated_image_path)  # Save the annotated image
            return send_from_directory(RESULT_FOLDER, file.filename)

if __name__ == "__main__":
    app.run(debug=True)
