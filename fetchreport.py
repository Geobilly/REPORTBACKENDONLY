from flask import Flask, jsonify
from flask_restful import Api, Resource
from flask_cors import CORS
import mysql.connector

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes
api = Api(app)

# MySQL database configuration
DB_HOST = '103.195.100.122'
DB_USER = 'kempsgra_report'
DB_PASSWORD = 'Billyabban@2000'
DB_DATABASE = 'kempsgra_reportsystem'  # Change to your actual database name

# Establish a connection to the MySQL database
db_connection = mysql.connector.connect(
    host=DB_HOST,
    user=DB_USER,
    password=DB_PASSWORD,
    database=DB_DATABASE
)

# Function to load all reports from the MySQL database
def load_all_reports():
    try:
        cursor = db_connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM report")
        reports = cursor.fetchall()
        cursor.close()
        return reports
    except Exception as e:
        print(f"Failed to fetch reports: {str(e)}")
        return []

# Resource for handling report fetching
class ReportFetchResource(Resource):
    def get(self):
        # Load all reports
        reports = load_all_reports()

        # Return the reports as JSON
        return jsonify(reports)

# Add resource to API with the desired endpoint name
api.add_resource(ReportFetchResource, '/fetch-reports')

if __name__ == '__main__':
    app.run(debug=True)
