import pandas as pd
from sklearn.preprocessing import OneHotEncoder, MinMaxScaler

# Load datasets
patients = pd.read_csv("patients.csv")
diagnoses = pd.read_csv("diagnoses_icd.csv")
procedures = pd.read_csv("procedures_icd.csv")
diagnoses_icd_code = pd.read_csv("d_icd_diagnoses.csv")

# Filter cancer-related diagnoses (example: ICD-10 codes starting with 'C')
cancer_diagnoses = diagnoses[diagnoses['icd_code'].str.startswith('C')]

# Merge with patient demographics
cancer_data = pd.merge(cancer_diagnoses, patients, on='subject_id')
final_cancer_data = pd.merge(cancer_data, diagnoses_icd_code, on='icd_code')

# One-hot encode cancer types
encoder = OneHotEncoder()
cancer_types_encoded = encoder.fit_transform(final_cancer_data[['icd_code']])

# Scale age
# scaler = MinMaxScaler()
# cancer_data['age_scaled'] = scaler.fit_transform(cancer_data[['age']])

# Save preprocessed data
final_cancer_data = final_cancer_data.rename(columns={"long_title": "diagnoses"})
final_cancer_data.to_csv("preprocessed_cancer_data.csv", index=False)
