import os
import json
import unicodedata
import multiprocessing
from multiprocessing import freeze_support
import concurrent.futures
import re
from neo4j import GraphDatabase
from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tqdm import tqdm

graphe=GraphDatabase.driver("bolt://localhost/:7687",auth=("neo4j","mathers22"))
def mr_service(gene):
    pathe='./amc/'+gene+'.json'
    with open(pathe,'r') as college_data:
      majors = json.load(college_data)
    
    

def openJson(name_tag):
    pathe='./amc/'+name_tag+'.json'
    with open(pathe,'r') as college_data:
      majors = json.load(college_data)
      return majors

def writeToJson(fileName,data):
   
    filePath='./amc/'+fileName+'.json'
    with open(filePath,'w') as fp:
        json.dump(data,fp)
subject_data_calendars=[]
def topic_to_db(courseU,topic_name,deg):
    course_name='"'+courseU+'"'
    topic='"'+topic_name+'"'
    degree_id='"'+deg+'"'
    sess=graphe.session()
    query="MATCH(x:CourseUnit{name:"+course_name+"}) CREATE(y:topic{name:"+topic+",deg:"+degree_id+"}),(x)-[:Topics_for]->(y)"
    sess.run(query)
    sess.close()

def search_jobs(search_subject,deg):
    data={}
    topic_list=[]
    youtube_data=[]
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
    driver = webdriver.Chrome(executable_path="../chromedriver", options=options)
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
                    topic_to_db(search_subject,td_topic,deg)
                    
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
                            
                            continue
                    except:
                        continue
                
                get_rid=topics_object.pop(0)
                

                for i in range(len(topics_object)):
                    
                    td_object=topics_object[i].find_elements_by_tag_name("td")
                    num_id=int(topic_int)
                
                    try:
                    
                        td_topic=td_object[num_id].get_attribute("innerText")
                        topic_list.append(td_topic)
                        topic_to_db(search_subject,td_topic,deg)

                        
                       
                    except:
                        continue
                                            



            except:
                print("no syllabus either")


        data["topics"]=topic_list
        data["vid_links"]=youtube_data
        subject_data_calendars.append(data)
    
    except:
      
        print("jokes")
      
    finally:
       driver.quit()



def dentist(jon):
  
    sess=graphe.session()
    jondoe=jon[0]
    toni=jon[1]
    degrees_name=jon[2]
    deg=jon[3]
    if(jondoe.split(' ',1)[0]=="or"):
        jondoe=jondoe.split(' ',1)[1]
    acutal_course_code=jondoe.split(" ")
                    
    period_course=acutal_course_code[0]+" "+acutal_course_code[1]
    
    contains_digit = any(map(str.isdigit, period_course))
    d=degrees_name
    course_unit='"'+jondoe+'"'

    if contains_digit == True:
        # print(value_for_extract[0][j])
        try:
            mr_service(jondoe)
            query="MATCH(x:Degree{name:"+d+"}) MERGE(y:CourseUnit{name:"+course_unit+"}) CREATE(x)-[:courses]->(y)"
            sess.run(query)
            sess.close()

        except:
            query="MATCH(x:Degree{name:"+d+"}) CREATE(y:CourseUnit{name:"+course_unit+"}),(x)-[:courses]->(y)"
            sess.run(query)
            sess.close()
        
            toni.append(jondoe)
            search_jobs(jondoe,deg)
            writeToJson(jondoe,subject_data_calendars)
           

           

def jobs(groupe):
   
    sub_path='./ad_sub/'+groupe
    manager= multiprocessing.Manager()
    return_dict= manager.list()    
  

  
    with open(sub_path,'r') as college_data:
        majors = json.load(college_data)

        for i in range(len(majors)):
            
            jon=list(majors[i].values())
            degrees_name=sorted(majors[i].keys())
            
         
            sess=graphe.session()
            d='"'+degrees_name[0]+'"'
            z='"'+str(jon[0])+'"'
            query="CREATE (X:Degree{name:"+d+"}),(y:syllabus_graph{name:"+d+",values:"+z+"}),(X)-[:instructions]->(y)"

            sess.run(query)
            sess.close()
            
            for x in range(len(jon[0])):
                
                value_for_extract=list(jon[0][x].values())
                
                # print(value_for_extract[0])
                items=((l,return_dict,d,value_for_extract[0].index(l))for l in value_for_extract[0])

              
                with multiprocessing.get_context('spawn').Pool() as pool:
                     pool.map(dentist, items)

    jole=list(return_dict)
    
    writeToJson('start_here',jole)
   
           
         
           

  
        
    


def main():
 
   
    jobs('Computer Science and Engineering (Course 6-​3).json')
  
  
    
    # Get_youtube()

if __name__ == '__main__':
    main()