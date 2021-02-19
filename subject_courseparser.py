import json 
from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import multiprocessing
import concurrent.futures
import time
import re
import json

with open('./subject_json/college.json','r') as college_data:
    majors = json.load(college_data)

def writeToJson(fileName,data):
    filePath='./major_json/'+fileName+'.json'
    with open(filePath,'w') as fp:
        json.dump(data,fp)

def starter():
    
    with concurrent.futures.ProcessPoolExecutor() as executor:
        future=executor.map(jeb,majors)



def jeb(maj):
    sub=maj["major"]
    urle=maj["major_link"]
    options = webdriver.ChromeOptions()
    options.headless = True
   
    options.add_argument("--window-size=1920,1080")
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--allow-running-insecure-content')
    options.add_argument("--disable-extensions")
    options.add_argument("--proxy-server='direct://'")
    options.add_argument("--proxy-bypass-list=*")
    options.add_argument("--start-maximized")
    options.add_argument('--disable-gpu')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--no-sandbox')
    driver = webdriver.Chrome(executable_path="/home/subodh/Desktop/rasa/chromedriver", options=options)

    url=urle
    driver.get(url)
    try:
        whole_college=[]
        element =WebDriverWait(driver,10).until(
        EC.presence_of_all_elements_located((By.ID,"sc_sccoursedescs"))
        )
        polo=element[0].find_elements_by_class_name("courseblock")
        for i in range(len(polo)):
            data={}
            major_block=polo[i].find_element_by_tag_name("strong")
            major_title=major_block.get_attribute("innerHTML")
            major_b_pre=polo[i].find_element_by_class_name("courseblockprereq")
            data["major_title"]=major_title
            data["major_preq"]=major_b_pre.get_attribute("innerText")
           
            whole_college.append(data)
            
          
        
    except:
        
        print("not_work")
    finally:
        writeToJson(sub,whole_college)
        driver.quit()



def main():
    starter()
if __name__ == '__main__':
    main()