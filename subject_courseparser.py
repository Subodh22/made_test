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

with open('./ad_sub/ad_lib.json','r') as college_data:
    majors = json.load(college_data)

# def writeToJson(fileName,data):
#     filePath='./ad_sub/'+fileName+'.json'
#     with open(filePath,'w') as fp:
#         json.dump(data,fp)

def starter():
    
    with concurrent.futures.ProcessPoolExecutor() as executor:
        future=executor.map(jeb,majors)


def subject_parser(cont):
   
   
    
    degree_table=[]
   
    
    
    for i in range(len(cont)):
        table_minor={}
    
        major_name=cont[i].find_elements_by_tag_name("h2")
       

        major_namer=major_name[0].get_attribute("innerHTML")
        
        minor_name =major_name[0].get_attribute("innerHTML")
        table_list=cont[i].find_elements_by_class_name("sc_courselist")
        
        req_name=cont[i].find_elements_by_tag_name("h3")
        
        req_namer=req_name[1].get_attribute("innerHTML")
        elective_subject=[]
        elective_type=""
        for j in range(1):
           
            data={}
            
            
            if(j>0):
                try:
                    req_namee=cont[i].find_elements_by_tag_name("h4")
                   
                    req_namer=req_namee[j-1].get_attribute("innerHTML")
                except:
                    header=req_namer
            
            header=req_namer
            
            sub_header=""
           
            actual_subjects=table_list[j].find_elements_by_tag_name("tr")
            list_subject=[]
                    
            
            for x in range(len(actual_subjects)):
                
                
                listed={}
                elective_table={}
                try:
                    
                    zucc=""
                   
                    essential_target="required"
                    jenny=actual_subjects[x].get_attribute("class")
                    button=actual_subjects[x].find_elements_by_tag_name("td")
                    java=button[0].get_attribute("innerText")
                    
                    if("lastrow" in jenny):
                        elective_table[elective_type]=list_subject
                        
                        elective_subject.append(elective_table)
                        listed[header]=java
                        listed["type"]=essential_target
                    
                    
                        list_subject.append(listed)
                        continue
                    try :

                        selection = actual_subjects[x].find_element_by_class_name("areasubheader")
                        essential_target="selection"
                        
                    except:
                        pass

                    if("areaheader" in jenny ):
                        
                        elective_table[elective_type]=list_subject
                        
                        elective_subject.append(elective_table)
                     
                        elective_type=java
                        
                        list_subject=[]
                       
                        continue
                    
                    listed[header]=java
                    listed["type"]=essential_target
                    
                    
                    list_subject.append(listed)
                    
                        
                


                   

                except:
                    print("joi")
        table_minor[minor_name]=elective_subject
        degree_table.append(table_minor)

    print(degree_table)

              

               
            


       
def jeb(maj):
    
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
    whole_college=[]
    try:
        
        element =WebDriverWait(driver,10).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME,"tab_content"))
        )
        print("joker")
        del element[0]
        
        subject_parser(element)
     
        
    except:
        element =WebDriverWait(driver,10).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME,"page_content"))
        )
        print("jokes")
        subject_parser(element)
       

        
            
        
        print("not_work")
    finally:
        # writeToJson(sub,whole_college)
        driver.quit()






def main():
    starter()
if __name__ == '__main__':
    main()