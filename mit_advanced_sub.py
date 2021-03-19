
from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import re
import json
# from neo4j import GraphDatabase

def writeToJson(fileName,data):
    filePath='./ad_sub/'+fileName+'.json'
    with open(filePath,'w') as fp:
        json.dump(data,fp)



def jeb():
    
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
    url="http://catalog.mit.edu/degree-charts/"
    driver.get(url)
    try:
        whole_college=[]
        element =WebDriverWait(driver,10).until(
        EC.presence_of_all_elements_located((By.ID,"/degree-charts/"))
        )
        list_major=element[0].find_elements_by_tag_name("a")
        
      

        for i in range(len(list_major)):
          
            data={}
            data["major_link"]=list_major[i].get_attribute("href")
            data["subject"]=list_major[i].get_attribute("innerText")
            whole_college.append(data)
       
        
    except:
        print("not_work")
    finally:
       
        writeToJson("college",whole_college)
        driver.quit()



def main():
    jeb()
if __name__ == '__main__':
    main()