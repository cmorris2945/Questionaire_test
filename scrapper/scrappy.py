from selenium import webdriver
from selenium.webdriver.common.by import By
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Doctor(Base):
    __tablename__ = 'doctors'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    designation = Column(String, nullable=False)
    profile_link = Column(String, nullable=False)


def scrapper_mdanderson(driver, url):
    try:
        driver.get(url)
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
                    designation=final_data[key]["designation"]
                )
                session.add(doctor)
            session.commit()
        else:
            print("No data to insert")
    except Exception as e:
        print("Error in inserting data to database {}".format(e))

if __name__ == "__main__":
    op = webdriver.ChromeOptions()
    op.add_argument('headless')
    driver = webdriver.Chrome(options=op)
    mdanderson_url = "https://faculty.mdanderson.org/search-results.html?searchType=faculty#filter|department:Department%20of%20Cancer%20Biology"
    stanford_url = "https://stanfordhealthcare.org/directory/directory.html#x1=sp_spec_care_phy&q1=true&sp_x_2=sp_dr_title_groups&sp_q_exact_2=Oncology&page=page-number"
    engine = create_engine('sqlite:///instance/patients-copy.db')
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    mdanderson_data = scrapper_mdanderson(driver, mdanderson_url)
    insert_data(mdanderson_data, session)
    stanford_data = scrapper_stanford(driver, stanford_url)
    insert_data(stanford_data, session)
    driver.close()
