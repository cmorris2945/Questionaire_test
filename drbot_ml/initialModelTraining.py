# import torch
# import torch.nn as nn
# import torch.optim as optim
# from torch.utils.data import DataLoader, Dataset
# import spacy
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import joblib

# # Define the model
# class SiameseNetwork(nn.Module):
#     def __init__(self, embedding_dim):
#         super(SiameseNetwork, self).__init__()
#         self.fc = nn.Sequential(
#             nn.Linear(embedding_dim, 128),
#             nn.ReLU(),
#             nn.Linear(128, 64),
#             nn.ReLU()
#         )

#     def forward_one(self, x):
#         return self.fc(x)

#     def forward(self, x1, x2):
#         out1 = self.forward_one(x1)
#         out2 = self.forward_one(x2)
#         return out1, out2

# # Contrastive Loss
# class ContrastiveLoss(nn.Module):
#     def __init__(self, margin=1.0):
#         super(ContrastiveLoss, self).__init__()
#         self.margin = margin

#     def forward(self, output1, output2, label):
#         euclidean_distance = nn.functional.pairwise_distance(output1, output2)
#         loss = torch.mean((1 - label) * torch.pow(euclidean_distance, 2) +
#                           label * torch.pow(torch.clamp(self.margin - euclidean_distance, min=0.0), 2))
#         return loss

# # Dataset for training pairs
# class DiagnosisDataset(Dataset):
#     def __init__(self, pairs, labels):
#         self.pairs = pairs
#         self.labels = labels

#     def __len__(self):
#         return len(self.pairs)

#     def __getitem__(self, idx):
#         return self.pairs[idx][0], self.pairs[idx][1], self.labels[idx]


# dataset = DiagnosisDataset(pairs, labels)
# dataloader = DataLoader(dataset, batch_size=1, shuffle=True)

# # Training loop
# model = SiameseNetwork(embedding_dim=2)
# criterion = ContrastiveLoss()
# optimizer = optim.Adam(model.parameters(), lr=0.001)

# for epoch in range(5):
#     for x1, x2, label in dataloader:
#         x1, x2, label = torch.tensor(x1, dtype=torch.float), torch.tensor(x2, dtype=torch.float), torch.tensor(label, dtype=torch.float)
#         optimizer.zero_grad()
#         out1, out2 = model(x1, x2)
#         loss = criterion(out1, out2, label)
#         loss.backward()
#         optimizer.step()


# Load the dataset
# Assuming your diagnosis data is in a CSV file
df = pd.read_csv("d_icd_diagnoses.csv")

# Drop duplicate rows
df_cleaned = df.drop_duplicates()

# Check for missing values
print(df_cleaned.isnull().sum())

# Fill or drop missing values (if any)
df_cleaned = df_cleaned.dropna()  # Drop rows with missing values
# Or use df_cleaned.fillna("Unknown") to fill missing values

df_cleaned = df_cleaned[df_cleaned['icd_code'].str.startswith('C')]
# Display cleaned data
print(f"Cleaned dataset: {len(df_cleaned)} records")
print(df_cleaned.head())

# Define cancer mappings for ICD-10 codes
icd10_to_cancer = {
    "C00": "Head and Neck Cancer",
    "C01": "Head and Neck Cancer",
    "C02": "Head and Neck Cancer",
    "C15": "Gastrointestinal Cancer",
    "C16": "Gastrointestinal Cancer",
    "C18": "Gastrointestinal Cancer",
    "C30": "Respiratory Cancer",
    "C50": "Breast Cancer",
    "C64": "Urinary Tract Cancer",
    "C81": "Lymphoma",
    "C82": "Non-Hodgkin Lymphoma",
    "C91": "Leukemia",
    "C92": "Leukemia",
    "D37": "Uncertain Neoplasm",
    "D38": "Uncertain Neoplasm",
    "C03": "Malignant neoplasm of gum",                       
    "C04": "Malignant neoplasm of floor of mouth",            
    "C05": "Malignant neoplasm of palate",                    
    "C06": "Malignant neoplasm of other parts of mouth",      
    "C07": "Malignant neoplasm of parotid gland",             
    "C08": "Malignant neoplasm of other salivary glands",     
    "C09": "Malignant neoplasm of tonsil",                    
    "C10": "Malignant neoplasm of oropharynx",                
    "C11": "Malignant neoplasm of nasopharynx",               
    "C12": "Malignant neoplasm of pyriform sinus",            
    "C13": "Malignant neoplasm of hypopharynx",               
    "C14": "Malignant neoplasm of other ill-defined sites",   
    "C17": "Malignant neoplasm of small intestine",           
    "C19": "Malignant neoplasm of rectosigmoid junction",     
    "C20": "Malignant neoplasm of rectum",                    
    "C21": "Malignant neoplasm of anus and anal canal",       
    "C22": "Malignant neoplasm of liver and intrahepatic bile ducts", 
    "C23": "Malignant neoplasm of gallbladder",               
    "C24": "Malignant neoplasm of other and unspecified parts of biliary tract", 
    "C25": "Malignant neoplasm of pancreas",                  
    "C26": "Malignant neoplasm of other digestive organs",    
    "C31": "Malignant neoplasm of accessory sinuses",         
    "C32": "Malignant neoplasm of larynx",                    
    "C33": "Malignant neoplasm of trachea",                   
    "C34": "Malignant neoplasm of bronchus and lung",         
    "C37": "Malignant neoplasm of thymus",                    
    "C38": "Malignant neoplasm of heart, mediastinum, and pleura", 
    "C39": "Malignant neoplasm of other respiratory organs",  
    "C40": "Malignant neoplasm of bone and articular cartilage of limbs", 
    "C41": "Malignant neoplasm of bone and articular cartilage of other sites", 
    "C43": "Malignant melanoma of skin",                      
    "C44": "Other malignant neoplasms of skin",               
    "C45": "Mesothelioma",                                    
    "C46": "Kaposi's sarcoma",                                
    "C47": "Malignant neoplasm of peripheral nerves",         
    "C48": "Malignant neoplasm of retroperitoneum and peritoneum", 
    "C49": "Malignant neoplasm of other connective tissues",  
    "C4A": "Merkel cell carcinoma",                           
    "C51": "Malignant neoplasm of vulva",                     
    "C52": "Malignant neoplasm of vagina",                    
    "C53": "Malignant neoplasm of cervix uteri",              
    "C54": "Malignant neoplasm of corpus uteri",              
    "C55": "Malignant neoplasm of uterus, part unspecified",  
    "C56": "Malignant neoplasm of ovary",                     
    "C57": "Malignant neoplasm of other female genital organs", 
    "C58": "Malignant neoplasm of placenta",                  
    "C60": "Malignant neoplasm of penis",                     
    "C61": "Malignant neoplasm of prostate",                  
    "C62": "Malignant neoplasm of testis",                    
    "C63": "Malignant neoplasm of other male genital organs", 
    "C65": "Malignant neoplasm of renal pelvis",              
    "C66": "Malignant neoplasm of ureter",                    
    "C67": "Malignant neoplasm of bladder",                   
    "C68": "Malignant neoplasm of other urinary organs",      
    "C69": "Malignant neoplasm of eye and adnexa",            
    "C70": "Malignant neoplasm of meninges",                  
    "C71": "Malignant neoplasm of brain",                     
    "C72": "Malignant neoplasm of spinal cord, cranial nerves, and other parts of CNS", 
    "C73": "Malignant neoplasm of thyroid gland",             
    "C74": "Malignant neoplasm of adrenal gland",             
    "C75": "Malignant neoplasm of other endocrine glands",    
    "C76": "Malignant neoplasm of other and ill-defined sites", 
    "C77": "Secondary and unspecified malignant neoplasm of lymph nodes", 
    "C78": "Secondary malignant neoplasm of respiratory and digestive organs", 
    "C79": "Secondary malignant neoplasm of other sites",     
    "C80": "Malignant neoplasm without specification of site", 
    "C81": "Hodgkin lymphoma",                                
    "C83": "Non-Hodgkin lymphoma",                            
    "C84": "Mature T/NK-cell lymphomas",                      
    "C85": "Other specified and unspecified types of non-Hodgkin lymphoma", 
    "C86": "Other specified types of T/NK-cell lymphoma",     
    "C88": "Malignant immunoproliferative diseases",          
    "C90": "Multiple myeloma and malignant plasma cell neoplasms", 
    "C93": "Monocytic leukemia",                              
    "C94": "Other leukemias of specified cell types",         
    "C95": "Leukemia of unspecified cell type",               
    "C96": "Other and unspecified malignant neoplasms of lymphoid, hematopoietic, and related tissue", 
    "C7A": "Malignant neuroendocrine tumors",                 
    "C7B": "Secondary neuroendocrine tumors",
    }                 

# Function to map ICD-10 codes to cancer types
def map_icd10_to_cancer(icd_code):
    prefix = icd_code[:3]  # Extract the first 3 characters
    return icd10_to_cancer.get(prefix, "Unknown")

# Apply mapping function
df_cleaned['cancer_type'] = df_cleaned['icd_code'].apply(map_icd10_to_cancer)

# Display results
print(df_cleaned.head())

# Save mapped dataset
# df_cleaned.to_csv("diagnosis_data_with_cancer_types.csv", index=False)



# Sample data (diagnosis and corresponding cancer types)
diagnoses = df_cleaned["long_title"]
cancer_types = df_cleaned["cancer_type"]

# Step 1: Preprocessing and Vectorization
vectorizer = TfidfVectorizer(stop_words='english')
X = vectorizer.fit_transform(diagnoses)  # Convert text to TF-IDF matrix
y = cancer_types  # Labels: cancer types

# Step 2: Split data into train/test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 3: Model Training
model = LogisticRegression()
model.fit(X_train, y_train)

# Step 4: Evaluate the model
y_pred = model.predict(X_test)
print(classification_report(y_test, y_pred))

# Step 5: Make predictions on new data
new_diagnosis = ["Malignant neoplasm of lung"]
new_data = vectorizer.transform(new_diagnosis)
prediction = model.predict(new_data)
print("Predicted Cancer Type:", prediction)

joblib.dump(model, 'cancer_type_classifier_model.pkl')  # Save the trained model
joblib.dump(vectorizer, 'vectorizer.pkl')  # Save the vectorizer
