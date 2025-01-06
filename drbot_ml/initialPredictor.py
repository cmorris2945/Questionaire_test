import joblib

# Load the saved model and vectorizer
model = joblib.load('cancer_type_classifier_model.pkl')
vectorizer = joblib.load('vectorizer.pkl')

# Example diagnosis to classify
# new_diagnosis = ["Malignant neoplasm of lung"]
new_diagnosis = ["hodgkin lymphoma"]

# Transform the input using the saved vectorizer
new_data = vectorizer.transform(new_diagnosis)

# Make predictions using the loaded model
prediction = model.predict(new_data)
print("Predicted Cancer Type:", prediction)

def build_query(cancer_type, db_connection):
    # Preprocess the cancer type (convert to lowercase)
    cancer_type = cancer_type[0].lower()
    
    # Split cancer type into individual words (keywords)
    keywords = cancer_type.split()
    
    # Construct the WHERE clause using LIKE for each keyword
    where_clause = " OR ".join([f"LOWER(speciality) LIKE '%{keyword}%'" for keyword in keywords])
    
    # Construct the MATCH SCORE part
    match_score_part = " + ".join([f"(LEN(LOWER(speciality)) - LEN(REPLACE(LOWER(speciality), '{keyword}', ''))) / LEN('{keyword}')" for keyword in keywords])
    
    # Final query with match score and sorting by the highest match score
    query = f"""
    SELECT doctors.*, 
           ({match_score_part}) AS match_score
    FROM doctors
    WHERE {where_clause}
    ORDER BY match_score DESC;
    """
    
    # Execute the query
    # cursor = db_connection.cursor()
    # cursor.execute(query)
    
    # # Fetch results
    # results = cursor.fetchall()
    
    return query

print(build_query(prediction, ""))