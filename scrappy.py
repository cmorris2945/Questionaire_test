from selenium import webdriver
from selenium.webdriver.common.by import By
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker
from bs4 import BeautifulSoup as bs
import urllib
import requests
import json

Base = declarative_base()

class Doctor(Base):
    __tablename__ = 'doctors'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    designation = Column(String, nullable=False)
    profile_link = Column(String, nullable=False)
    education_experience_summary = Column(String)

def scrape_profile_data_mdanderson(driver, url):
    driver.get(url)
    driver.implicitly_wait(5)
    result = driver.find_elements(By.CSS_SELECTOR, '.accordion-content-left.accordion-content.col12')[1]
    # for r in result:
    elements = result.find_elements(By.TAG_NAME, 'table')
    # for element in elements:
    experience_text = []
    for i in range(0,2):
        tr = elements[i].find_elements(By.TAG_NAME, 'tr')
        for t in tr:
            td = t.find_elements(By.TAG_NAME, 'td')
            for single in td:
                print("tag_name: {}".format(single.tag_name))
                print("text: {}".format(single.text))
                experience_text.append(single.text)

    final_list = [experience_text[i] + " " + experience_text[i + 1] 
       for i in range(0, len(experience_text), 2)]
    return final_list

def scrape_profile_data_stanford(url):
    profile_data = {}
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception("response is not 200")
    html = bs(response.text, 'html.parser')
    bio = html.find('div', class_='bio-txt-section')
    if bio != None:
        profile_data['bio'] = bio.text.strip().split('\n')[0]
    education = html.find(id='professionalEducation')
    if education != None:
        profile_data['education'] = []
        for li in education.find_all('li'):
            profile_data['education'].append(li.text)
    specializingIn = html.find(id="specializingIn")
    if specializingIn != None:
        profile_data['specializeIn'] = []
        for li in specializingIn.find_all('li'):
            profile_data['specializeIn'].append(li.text)
    return profile_data

def scrapper_mdanderson(driver, url):
    try:
        driver.get(url)
        driver.implicitly_wait(5)
        print("scrapping from url: {}".format(url))
        results = driver.find_elements(By.CLASS_NAME, 'faculty-result')
        final_data = {}
        for index, result in enumerate(results):
            res = result.find_elements(By.CSS_SELECTOR, '*')
            final_data[index] = {}
            for single in res:
                if single.tag_name == 'p':
                    # Storing the whole text because some profiles were missing the title
                    # i.e Professor, Assistant Professor
                    final_data[index]['designation'] = single.text
                if single.tag_name == 'a':
                    final_data[index]["name"] = single.text
                    final_data[index]["profile_link"] = single.get_attribute('href')
        for key in final_data:
            final_data[key]["education_experience_summary"] = scrape_profile_data_mdanderson(driver, final_data[key]["profile_link"])
            print("Done profile scrapping for: {}".format(final_data[key]["name"]))
        print("scrapping complete for mdanderson...")
        return final_data
    except Exception as e:
        print("Error in scrapping data {}".format(e))
        return {}

def scrapper_stanford(driver, url):
    try: 
        final_data = {}
        index = 0
        for i in range(1,10):
            updated_url = url.replace("page-number", str(i))
            driver.get(updated_url)
            driver.implicitly_wait(5)
            print("scrapping from url: {}".format(updated_url))
            results = driver.find_elements(By.CSS_SELECTOR, ".physicianSearchResult.col-sm-12")
            for result in results:
                res = result.find_elements(By.CSS_SELECTOR, '*')
                final_data[index] = {}
                designation = {
                    "speciality": "",
                    "title": ""
                }
                for single in res:
                    if single.get_attribute("class") == 'doctor-specialty-small':
                        designation["speciality"] = single.text
                    if single.get_attribute("class") == 'academic-title-small':
                        designation["title"] = single.text
                    # if single.tag_name == 'a':
                    if single.get_attribute("class") == 'doctor-name':
                        final_data[index]["name"] = single.text
                        final_data[index]["profile_link"] = single.get_attribute('href')
                if designation["title"] != "":
                    final_data[index]["designation"] = designation["title"] + ", " + designation["speciality"]
                else:
                    final_data[index]["designation"] = designation["speciality"]
                
                education_experience_summary_data = scrape_profile_data_stanford(final_data[index]["profile_link"])
                final_data[index]["education_experience_summary"] = json.dumps(education_experience_summary_data)
                print("profile data extracted for doctor: {}".format(final_data[index]["name"]))
                
                index += 1
        print("scrapping complete for stanford...")
        return final_data
    except Exception as e:
        print("Error in scrapping data {}".format(e))
        return {}

def insert_data(final_data, session):
    try:
        if final_data:
            for key in final_data:
                doctor = Doctor(
                    name= final_data[key]["name"],
                    profile_link=final_data[key]["profile_link"],
                    designation=final_data[key]["designation"],
                    education_experience_summary=final_data[key]["education_experience_summary"]
                )
                session.add(doctor)
            session.commit()
        else:
            print("No data to insert")
    except Exception as e:
        print("Error in inserting data to database {}".format(e))

if __name__ == "__main__":
    op = webdriver.ChromeOptions()
    op.add_argument('--headless=new')
    op.add_argument('--disable-gpu')
    driverChrome = webdriver.Chrome(options=op)
    mdanderson_url = "https://faculty.mdanderson.org/search-results.html?searchType=faculty#filter|department:Department%20of%20Cancer%20Biology"
    stanford_url = "https://stanfordhealthcare.org/directory/directory.html#x1=sp_spec_care_phy&q1=true&sp_x_2=sp_dr_title_groups&sp_q_exact_2=Oncology&page=page-number"
    
    
    server = 'drbotserver.database.windows.net'
    database = 'drbothealthdb'
    username = 'drbot'
    password = 'AquaMan40!@'  # Actual password from the connection string
    driver = '{ODBC Driver 18 for SQL Server}'  # Ensure this matches the installed driver

    # Create the connection string
    params = urllib.parse.quote_plus(
        f'DRIVER={driver};SERVER={server};DATABASE={database};UID={username};PWD={password};Encrypt=yes;TrustServerCertificate=no;Connection Timeout=60;'
        )
    # For mssql database 
    # engine = create_engine(f"mssql+pyodbc:///?odbc_connect={params}")
    
    # For local database
    engine = create_engine('sqlite:///instance/patients-copy.db')
    
    
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    # mdanderson_data = scrapper_mdanderson(driverChrome, mdanderson_url)
    # insert_data(mdanderson_data, session)
    stanford_data = scrapper_stanford(driverChrome, stanford_url)
    insert_data(stanford_data, session)
    driverChrome.close()
