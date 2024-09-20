# app.py

from flask import Flask, render_template, request, redirect, url_for
from database import db, init_db, Patient  # Import from database.py
import traceback
from flask_migrate import Migrate

# Initialize Flask app
app = Flask(__name__)

# Initialize the database
init_db(app)
migrate = Migrate(app, db)  # Add this line to initialize Flask-Migrate

# Route for the main page
@app.route('/', methods=['GET', 'POST'])
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
                doctor_preferences=data.get('doctor_preferences')
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