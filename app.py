# app.py
from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory patient storage
patients = []

@app.route('/')
def home():
    return "Welcome to the Patient Management System!"

# Get all patients
@app.route('/patients', methods=['GET'])
def get_patients():
    return jsonify(patients)

# Add a new patient
@app.route('/patients', methods=['POST'])
def add_patient():
    data = request.get_json()
    if not data.get("name") or not data.get("age") or not data.get("symptoms"):
        return jsonify({"error": "Missing patient information"}), 400
    patients.append(data)
    return jsonify({"message": "Patient added successfully"}), 201

# Get a single patient by index
@app.route('/patients/<int:index>', methods=['GET'])
def get_patient(index):
    if 0 <= index < len(patients):
        return jsonify(patients[index])
    return jsonify({"error": "Patient not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
