from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configure SQLite database (or use PostgreSQL if needed)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///reports.db'
db = SQLAlchemy(app)

# Report Model
class Report(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    department = db.Column(db.String(50), nullable=False)
    member = db.Column(db.String(100), nullable=False)
    task = db.Column(db.String(500), nullable=False)

# Route to add a report
@app.route('/add_report', methods=['POST'])
def add_report():
    data = request.json
    new_report = Report(department=data['department'], member=data['member'], task=data['task'])
    db.session.add(new_report)
    db.session.commit()
    return jsonify({'message': 'Report added successfully'})

# Route to fetch reports
@app.route('/get_reports', methods=['GET'])
def get_reports():
    reports = Report.query.all()
    output = [{'id': r.id, 'department': r.department, 'member': r.member, 'task': r.task} for r in reports]
    return jsonify(output)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Create database
    app.run(debug=True)
