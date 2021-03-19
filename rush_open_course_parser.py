import os
import json
import unicodedata
import multiprocessing
import concurrent.futures
import re
from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def mr_service(gene):
    pathe='./amc/'+gene+'.json'
    with open(pathe,'r') as college_data:
      majors = json.load(college_data)
      print("recorded")

def writeToJson(fileName,data):
   
    filePath='./amc/'+fileName+'.json'
    with open(filePath,'w') as fp:
        json.dump(data,fp)
subject_data_calendars=[]
aftermath_calender=[]
def search_jobs(search_subject):
    data={}
    topic_list=[]
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
    url="https://ocw.mit.edu/search/ocwsearch.htm?q="+search_subject
    driver.get(url)
    try:
       
        
        element = WebDriverWait(driver,10).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME,"gs-title"))
        )
       
        data[search_subject]=element[1].get_attribute("href")
        url_core=element[1].get_attribute("href")
        url_calendar=url_core+"calendar"
        driver.get(url_calendar)
        try:
            element = WebDriverWait(driver,10).until(
            EC.presence_of_all_elements_located((By.ID,"course_inner_section"))
            )
            topic_int=""
          
            calendar_table=element[0].find_elements_by_tag_name("table")
           
            topics_object = calendar_table[0].find_elements_by_tag_name("tr")
           
            t_head=topics_object[0].find_elements_by_tag_name("th")
            
            for i in range(len(t_head)):
                try:
                    heads=(t_head[i].get_attribute("innerText")).lower()
                    if("topic" in heads):
                        topic_int=i
                        print(topic_int)
                        break
                except:
                    continue
            
            get_rid=topics_object.pop(0)
            

            for i in range(len(topics_object)):
                
                td_object=topics_object[i].find_elements_by_tag_name("td")
                num_id=int(topic_int)
              
                try:
                   
                    td_topic=td_object[num_id].get_attribute("innerText")
                    topic_list.append(td_topic)
                except:
                    continue
                
       


        except:
            print("no calendar here")
            url_syllabus=url_core+"syllabus"
            driver.get(url_syllabus)
            
            try:
                
              
                element = WebDriverWait(driver,10).until(
                EC.presence_of_all_elements_located((By.ID,"course_inner_section"))
                )
                topic_int=""
            
                calendar_table=element[0].find_elements_by_tag_name("table")
                
                topics_object = calendar_table[1].find_elements_by_tag_name("tr")
               
                t_head=topics_object[0].find_elements_by_tag_name("th")
                
                for i in range(len(t_head)):
                    try:
                        heads=(t_head[i].get_attribute("innerText")).lower()
                        if("topic" in heads):
                            topic_int=i
                            print(topic_int)
                            break
                    except:
                        continue
                
                get_rid=topics_object.pop(0)
                

                for i in range(len(topics_object)):
                    
                    td_object=topics_object[i].find_elements_by_tag_name("td")
                    num_id=int(topic_int)
                
                    try:
                    
                        td_topic=td_object[num_id].get_attribute("innerText")
                        topic_list.append(td_topic)
                    except:
                        continue
                    



            except:
                print("no syllabus either")


        data["topics"]=topic_list
        subject_data_calendars.append(data)
    
    except:
      
        print("jokes")
      
    finally:
       driver.quit()

def dentist(jon):
   
    jondoe=jon[0]
    toni=jon[1]
    if(jondoe.split(' ',1)[0]=="or"):
        jondoe=jondoe.split(' ',1)[1]
    acutal_course_code=jondoe.split(" ")
                    
    period_course=acutal_course_code[0]+" "+acutal_course_code[1]
    
    contains_digit = any(map(str.isdigit, period_course))
    

    if contains_digit == True:
        # print(value_for_extract[0][j])
        try:
            mr_service(jondoe)

        except:
          
            toni.append(jondoe)
            search_jobs(jondoe)
            
            writeToJson(jondoe,subject_data_calendars)
            subject_data_calendats=[]

manager= multiprocessing.Manager()
return_dict= manager.list()    



def jobs(groupe):
   
    sub_path='./ad_sub/'+groupe
    
    with open(sub_path,'r') as college_data:
        majors = json.load(college_data)

        for i in range(len(majors)):
            
            jon=list(majors[i].values())
            for x in range(len(jon[0])):
                
                value_for_extract=list(jon[0][x].values())
                # print(value_for_extract[0])
                items=((l,return_dict)for l in value_for_extract[0])
                with concurrent.futures.ProcessPoolExecutor() as executor:
                  future=executor.map(dentist,items)
                
                   
        
    print(return_dict)
    
    




def starter():
    # path, dirs, files = next(os.walk("./ad_sub/"))
    # file_count = len(files)
    
    # with concurrent.futures.ProcessPoolExecutor() as executor:
    #     future=executor.map(jobs,files)
    jobs('Business Analytics (Course 15-​2).json')



starter()