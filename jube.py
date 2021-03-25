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
from tqdm import tqdm
import pandas as pd
from multiprocessing import Pool
from concurrent.futures import TimeoutError
from multiprocessing import cpu_count



def Get_youtube(lister):
    try:
        topic=lister[1]
        subject=lister[0]
        # youtube_data=[]
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
        urle="https://www.youtube.com/results?search_query="+topic
        driver.get(urle)
        # youtube_data=lister[2]
        rank=lister[3]
        # u_data=[]
   
   
       
        elemente =WebDriverWait(driver,10).until(
        EC.presence_of_all_elements_located((By.ID,"dismissible"))
        ) 
      
        driver.execute_script("window.scrollTo(0, 800)") 
        
        driver.execute_script("window.scrollTo(0, 1980)") 

       
        
        for i in tqdm(range(15)):
            
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
            vid_det["subject"]=subject
            # u_data.append(vid_det)
            # vids=list(u_data.values())
            # print(vid_det)
            df2 = pd.DataFrame(columns=["degree","video_id","duration","views","age","title","img","topic","subject"])
    
            
            df2=df2.append(vid_det,ignore_index=True)
            df2.to_csv('./pending/'+subject+'.csv', mode='a', header=False)
            print("okok")
       
        print(subject+"donezo")
        driver.quit()   
            
   
   
  
    except:
        print("not_work")
    
  




def openJson(name_tag):
    pathe='./amc/'+name_tag+'.json'
    with open(pathe,'r') as college_data:
      majors = json.load(college_data)
      return majors
manager= multiprocessing.Manager()
def june_bug(name_tag):
    work_data={}
    
    
    majors=[]
    pathe='./amc/'+name_tag+'.json'
    with open(pathe,'r') as college_data:
      majors = json.load(college_data)
    if(majors!=[]):
        for i in range(len(majors)):
            data_json=openJson(majors[i])
            
            your_data=manager.dict()
            df = pd.DataFrame(columns=["degree","video_id","duration","views","age","title","img","topic","subject"])
            df.to_csv('./pending/'+majors[i]+'.csv')
            if(data_json!=[]):
                work_data=data_json[0]
                if(len(data_json)>1):
                    work_data=data_json[1]
                item=((majors[i],s,0,work_data["topics"].index(s))for s in work_data["topics"])
                
                with concurrent.futures.ProcessPoolExecutor(max_workers=10) as executor:
                    future=executor.map(Get_youtube,item,timeout=20)
                with multiprocessing.get_context('spawn').Pool() as pool:
                    pool.map(Get_youtube, item)
            
            
  

if __name__=="__main__":
    june_bug('start_here')

