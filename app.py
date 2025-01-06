# app.py

from flask import Flask, render_template, request, redirect, url_for
from database import db, init_db, Patient, ContactForm, Subscribe, InquiryWithin  # Import from database.py
import traceback
from flask_migrate import Migrate
from sqlalchemy import func
from datetime import datetime
from flask_mail import Mail, Message
from email_templates import subscribe_template, inquiry_template, contact_template
# Initialize Flask app
app = Flask(__name__)

# Initialize the database
init_db(app)
migrate = Migrate(app, db)  # Add this line to initialize Flask-Migrate

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'info@drbot.health'
app.config['MAIL_PASSWORD'] = 'AllNewPassword@111!9.'
app.config['MAIL_DEFAULT_SENDER'] = 'info@drbot.health'

# Initialize Flask-Mail
mail = Mail(app)

@app.route('/', methods=['GET'])
def indexPHP():
    return render_template('index-php.html')

@app.route('/contact', methods=['POST'])
def contact_us():
    try:
        if request.method == "POST":
            data = {}
            count = db.session.query(func.count(ContactForm.id)).scalar()
            data["email"] = email = request.form["email"]
            data["message"] = message = request.form["message"]
            current_date = datetime.now()
            created_date = current_date.strftime("%Y-%m-%d")
            id = count + 1010
            contact = ContactForm(id=id, email=email, message=message, created_date=created_date)
            db.session.add(contact)
            db.session.commit()
            
            email_body = contact_template.format(**data)
            msg = Message(
                subject="DRBOT: New Contact Inquiry",
                recipients=["kanu@drbot.health"],
                cc=["kanua1@icloud.com"],
                bcc=["info@drbot.health"],
                html=email_body  # HTML content
            )
            mail.send(msg)
        return render_template('index-php.html')
    except Exception as e:
        print(e)
        return render_template('index-php.html')

@app.route('/subscribe', methods=["POST"])
def subscribe():
    try:
        if request.method == "POST":
            data = {}
            count = db.session.query(func.count(Subscribe.id)).scalar()
            data["email"] = email = request.form["email"]
            current_date = datetime.now()
            created_date = current_date.strftime("%Y-%m-%d")
            id = count + 1010
            sub = Subscribe(id=id, email_subscribe=email, created_date=created_date)
            db.session.add(sub)
            db.session.commit()

            email_body = subscribe_template.format(**data)
            msg = Message(
                    subject="DRBOT: New Subscriber",
                    recipients=["kanu@drbot.health"],
                    cc=["kanua1@icloud.com"],
                    bcc=["info@drbot.health"],
                    html=email_body  # HTML content
                )
            mail.send(msg)
        return render_template('index-php.html')
    except Exception as e:
        print(e)
        return render_template('index-php.html')

@app.route('/inquiry_within', methods=["POST"])
def inquiry_within():
    try:
        if request.method == "POST":
            data = {}
            count = db.session.query(func.count(InquiryWithin.id)).scalar()
            data["name"] = name = request.form['name']
            data["location"] = location = request.form['location']
            data["age"] = age = request.form['age']
            data["email"] = email = request.form['email']
            data["gender"] = gender = request.form['gender']
            data["relation"] = relation = request.form['relation']
            data["diagnosis"] = diagnosis = request.form['diagnosisType']
            data["specify_location_of_cancer"] = specify_location_of_cancer = request.form['locationInput']
            data["insurance"] = insurance = request.form['insurance']
            data["mobile_number"] = mobile_number = request.form['mobile_number']
            data["testing"] = testing = request.form.get('testing', 'no')
            data["tests"] = tests = request.form.get('tests', '')
            data["opinion"] = opinion = request.form['opinion']
            data["noOpinionReason"] = noOpinionReason = request.form.get('noOpinionReason', '')
            data["interested"] = interested = request.form['interested']
            data["remark"] = remark = request.form['remark']
            data["discussion"] = discussion = request.form.get('discussion', '')
            current_date = datetime.now()
            created_date = current_date.strftime("%Y-%m-%d")
            enq_id = 10000 + count
            inquiry = InquiryWithin(id=enq_id, enq_id=enq_id,name=name,location=location,
                                    age=age, email=email, mobile_number=mobile_number, gender=gender,
                                    relation=relation, diagnosis=diagnosis, specify_location_of_cancer=specify_location_of_cancer,
                                    testing=testing, tests=tests, insurance=insurance, opinion=opinion,
                                    noOpinionReason=noOpinionReason, interested=interested,
                                    discussion=discussion, remark=remark, date=created_date)
            db.session.add(inquiry)
            db.session.commit()

            email_body = inquiry_template.format(**data)
            msg = Message(
                        subject="DRBOT: New Patient Inquiry #{}".format(enq_id),
                        recipients=["kanu@drbot.health"],
                        cc=["kanua1@icloud.com"],
                        bcc=["info@drbot.health"],
                        html=email_body  # HTML content
                    )
            mail.send(msg)
            return redirect(url_for('index'))
        else:
            return render_template('index-php.html')
    except Exception as e:
        print(e)
        return render_template('index-php.html')
# Route for the main page
@app.route('/index', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        try:
            # Print out all form data
            print("Received form data:")
            for key, value in request.json.items():
                print(f"{key}: {value}")
            data = request.json
            # Process form submission
            new_patient = Patient(
                name=data.get('name'),
                age=data.get('age'),
                stage=data.get('stage'),
                previous_treatments=data.get('previous_treatments'),
                preferred_language=data.get('preferred_language'),
                location=data.get('location'),
                family_history=data.get('family_history'),
                genetic_testing=data.get('genetic_testing'),
                help_today=data.get('help_today'),
                help_option=data.get('help_option'),
                second_opinion=data.get('second_opinion'),
                started_treatment=data.get('started_treatment'),
                zip_code=data.get('zip_code'),
                insurance_name=data.get('insurance_name'),
                gender=data.get('gender'),
                confirm_info=data.get('confirm_info'),
                religiosity=data.get('religiosity'),
                immigration_status=data.get('immigration_status'),
                ethnicity=data.get('ethnicity'),
                social_support=data.get('social_support'),
                treatment_approach=data.get('treatment_approach'),
                doctor_preferences=data.get('doctor_preferences'),
                # selected_doctor = data.get('selected_doctor')
            )
            db.session.add(new_patient)
            db.session.commit()
            return redirect(url_for('thank_you'))
        except Exception as e:
            print(f"An error occurred: {str(e)}")
            print(traceback.format_exc())
            return "An error occurred while processing your request.", 400
    return render_template('index.html')

# Route for the thank you page
@app.route('/thank-you')
def thank_you():
    return render_template('thank_you.html')

# Run the app
if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Create tables if they don't exist
    app.run(debug=True, host='0.0.0.0')  # Set debug=True for more detailed error messages