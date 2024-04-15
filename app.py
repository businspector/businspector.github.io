from flask import Flask, render_template, request, jsonify
from datetime import datetime, timedelta
import json

app = Flask(__name__)

# This will store the reports in memory
reports = []

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/report', methods=['POST'])
def report():
    data = request.json
    # Add a timestamp to each report
    data['timestamp'] = datetime.now()
    reports.append(data)
    return jsonify(success=True)

@app.route('/reports')
def get_reports():
    # Remove reports older than 10 minutes
    current_time = datetime.now()
    global reports
    reports = [report for report in reports if current_time - report['timestamp'] < timedelta(minutes=10)]
    return jsonify(reports)

if __name__ == '__main__':
    app.run(debug=True)
