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
aftermath_calender=[]
def search_jobs(search_subject):
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

def Get_youtube(lister):
    topic=lister[1]
    subject=lister[0]
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
    driver = webdriver.Chrome(executable_path="/home/subodh/Desktop/rasa/chromedriver", options=options)
    urle="https://www.youtube.com/results?search_query="+topic+"in="+subject
    driver.get(urle)
    youtube_data=lister[2]
    rank=lister[3]
    u_data=[]
    print(rank)
    try:
        elemente =WebDriverWait(driver,10).until(
        EC.presence_of_all_elements_located((By.ID,"dismissible"))
        ) 
      
        driver.execute_script("window.scrollTo(0, 800)") 
        
        driver.execute_script("window.scrollTo(0, 1980)") 
       
        for i in range(15):
            
            vid_det={}
            vid_det["degree"]=lister[3]
            vid_det["video_id"]=re.findall(r"watch\?v=(\S{11})",(elemente[i].find_element_by_id("thumbnail").get_attribute("href")))


            toni = elemente[i].find_element_by_tag_name("yt-formatted-string").get_attribute("aria-label")
           
            result = re.search('ago(.*)views', toni)
            
            
            ioi=" ".join((result.group(1)).split(" ")[:-2])
            


            
            tolir=elemente[i].find_element_by_id("metadata-line")
          
            
    
            toli=tolir.find_elements_by_tag_name("span")
            
            
            vid_det["duration"]=ioi
            vid_det["views"]=toli[0].get_attribute("innerHTML")
            vid_det["age"]=toli[1].get_attribute("innerHTML")
          
            vid_det["title"]=elemente[i].find_element_by_tag_name("yt-formatted-string").get_attribute("innerHTML")
           
            vid_det["img"]=elemente[i].find_element_by_id("img").get_attribute("src")
            
            vid_det["topic"]=topic

            u_data.append(vid_det)
        
    

           
            
    except:
        print("not_work")

    youtube_data[topic]=u_data
    

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
            # subject_data_calendars=[]

            

manager= multiprocessing.Manager()
return_dict= manager.list()    
your_data=manager.dict()


def jobs(groupe):
   
    sub_path='./ad_sub/'+groupe
    work_data={}
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
                
    for i in range(len(return_dict)):
        data_json=openJson(return_dict[i])
        work_data=data_json[0]
        if(len(data_json)>1):
            work_data=data_json[1]
        items=((return_dict[i],s,your_data,work_data["topics"].index(s))for s in work_data["topics"])
        with concurrent.futures.ProcessPoolExecutor() as executor:
            future=executor.map(Get_youtube,items)
       
        
        maj={}
        pather='./amc/'+return_dict[i]+'.json'
        with open(pather,'r') as collegee_data:
            maj = json.load(collegee_data)
        j=your_data.copy()
        po=[]
        po.append(j)
        # print(po)
        maj[0]["vid"]=po
        # print(maj)
        j_obj=open(pather,"w")
        json.dump(maj,j_obj)
        j_obj.close()
        
            
  
        
    



def starter():
    # path, dirs, files = next(os.walk("./ad_sub/"))
    # file_count = len(files)
    
    # with concurrent.futures.ProcessPoolExecutor() as executor:
    #     future=executor.map(jobs,files)
    jobs('Business Analytics (Course 15-​2).json')
    # Get_youtube()



starter()