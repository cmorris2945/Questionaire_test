import pandas as pd
from sqlalchemy import create_engine
import urllib

server = 'drbotserver.database.windows.net'
database = 'drbothealthdb'
username = 'drbot'
password = 'AquaMan40!@'  # Actual password from the connection string
driver = '{ODBC Driver 18 for SQL Server}'  # Ensure this matches the installed driver

params = urllib.parse.quote_plus(
    f'DRIVER={driver};SERVER={server};DATABASE={database};UID={username};PWD={password};Encrypt=yes;TrustServerCertificate=no;Connection Timeout=60;'
)
connection_string = f"mssql+pyodbc:///?odbc_connect={params}"
# engine = create_engine(connection_string, echo=True)
data = pd.read_csv("/home/ahmad/Downloads/mayoclinic-1.csv")

data = data.rename(columns={"profile-link": "profile_link"})
data["speciality"] = data[["Speciality-1", "Speciality-2", "Speciality-3", "Speciality-4"]].fillna("").agg(",".join, axis=1)
data = data[["name", "profile_link", "designation", "location", "speciality"]]
data["speciality"] = data["speciality"].str.strip(",")
data["speciality"] = data["speciality"].str.replace(",,", ",", regex=False)
data["designation"] = data["designation"].fillna("Oncologist")

# print(data["speciality"].head(10))



# data.to_sql(
#     name='doctors', 
#     con=engine, 
#     if_exists='append',
#     index=False
#     )
print(data[data["speciality"].str.contains("non-Hodgkin", case=False)])