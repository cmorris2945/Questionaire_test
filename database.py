# database.py

from flask_sqlalchemy import SQLAlchemy
import urllib

# Configure Azure SQL Database connection
server = 'drbotserver.database.windows.net'
database = 'drbothealthdb'
username = 'drbot'
password = 'AquaMan40!@'  # Actual password from the connection string
driver = '{ODBC Driver 18 for SQL Server}'  # Ensure this matches the installed driver

# Create the connection string
params = urllib.parse.quote_plus(
    f'DRIVER={driver};SERVER={server};DATABASE={database};UID={username};PWD={password};Encrypt=yes;TrustServerCertificate=no;Connection Timeout=60;'
)

# Configure SQLAlchemy
db = SQLAlchemy()

def init_db(app):
    app.config['SQLALCHEMY_DATABASE_URI'] = f"mssql+pyodbc:///?odbc_connect={params}"
    # app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///patients-copy.db"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)

# Define Patient model
class Patient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    stage = db.Column(db.String(50), nullable=False)
    previous_treatments = db.Column(db.String(200))
    preferred_language = db.Column(db.String(50))
    location = db.Column(db.String(100))
    family_history = db.Column(db.String(50))
    genetic_testing = db.Column(db.String(50))
    help_today = db.Column(db.String(100))
    help_option = db.Column(db.String(100))
    second_opinion = db.Column(db.String(10))
    started_treatment = db.Column(db.String(10))
    zip_code = db.Column(db.String(20))
    insurance_name = db.Column(db.String(50))
    gender = db.Column(db.String(20))
    confirm_info = db.Column(db.String(10))
    religiosity = db.Column(db.String(50))
    immigration_status = db.Column(db.String(50))
    ethnicity = db.Column(db.String(50))
    social_support = db.Column(db.String(50))
    treatment_approach = db.Column(db.String(100))
    doctor_preferences = db.Column(db.String(100))
    # selected_doctor = db.Column(db.String(100))

class ContactForm(db.Model):
    __tablename__= "contact_form"

    id = db.Column(db.Integer, primary_key=True, autoincrement=False)
    email = db.Column(db.String(100))
    message = db.Column(db.Text)
    created_date = db.Column(db.String(20))

class Subscribe(db.Model):
    __tablename__= "subsribe"

    id = db.Column(db.Integer, primary_key=True, autoincrement=False)
    email_subscribe = db.Column(db.String(50))
    created_date = db.Column(db.String(20))

class InquiryWithin(db.Model):
    __tablename__= "inquiry_within"

    id = db.Column(db.Integer, primary_key=True, autoincrement=False)
    enq_id = db.Column(db.Integer)
    name = db.Column(db.String(50))
    mobile_number = db.Column(db.String(50)) 
    specify_location_of_cancer = db.Column(db.String(50)) 
    insurance = db.Column(db.String(50))
    remark = db.Column(db.String(50))
    location = db.Column(db.String(50))
    age = db.Column(db.String(50))
    email = db.Column(db.String(50))
    gender = db.Column(db.String(50))
    relation = db.Column(db.String(50))
    diagnosis = db.Column(db.String(50))
    testing = db.Column(db.String(50))
    tests = db.Column(db.String(50))
    opinion = db.Column(db.String(50))
    noOpinionReason = db.Column(db.String(50))
    interested = db.Column(db.String(50))
    discussion = db.Column(db.String(50))
    date = db.Column(db.String(50))