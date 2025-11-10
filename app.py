from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

# Database setup
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'patients.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Patient model
class Patient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    symptoms = db.Column(db.String(200), nullable=False)

# Routes
@app.route('/')
def index():
    patients = Patient.query.all()
    return render_template('index.html', patients=patients)

@app.route('/add', methods=['POST'])
def add_patient():
    name = request.form.get('name')
    age = request.form.get('age')
    symptoms = request.form.get('symptoms')
    if name and age and symptoms:
        patient = Patient(name=name, age=int(age), symptoms=symptoms)
        db.session.add(patient)
        db.session.commit()
    return redirect('/')

# Create database tables if not exist
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
