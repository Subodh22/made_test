# import urllib.request
# from lxml import html
# import re 
# htmle = urllib.request.urlopen("https://www.youtube.com/results?search_query=rsa+algorithm+in+number+theory")
# tree=htmle.read().decode('utf8')
# htmltee=html.fromstring(tree)
# video_ids = re.findall(r"watch\?v=(\S{11})",htmle.read().decode())
# print(htmltee)
from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import re
from neo4j import GraphDatabase



def jeb(jole):
    options = webdriver.ChromeOptions()
    options.headless = True
    youtube_data=[]
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
    
   
    subject=jole[0].replace(" ","+")
    topic=jole[1].replace(" ","+")
    
    
    url="https://www.youtube.com/results?search_query="+topic+"in="+subject
    driver.get(url)
    try:
        element =WebDriverWait(driver,10).until(
        EC.presence_of_all_elements_located((By.ID,"dismissable"))
        )
        driver.execute_script("window.scrollTo(0, 800)") 
        
        driver.execute_script("window.scrollTo(0, 1980)") 
        for i in range(20):
            vid_det={}
            vid_det["degree"]=i
            vid_det["video_id"]=re.findall(r"watch\?v=(\S{11})",(element[i].find_element_by_id("thumbnail").get_attribute("href")))
            vid_det["title"]=element[i].find_element_by_tag_name("yt-formatted-string").get_attribute("aria-label")
            vid_det["img"]=element[i].find_element_by_id("img").get_attribute("src")
            vid_det["topic"]=jole[1]
            youtube_data.append(vid_det)
        
    except:
        print("not_work")
    finally:
        driver.quit()
    mer_list=youtube_data
    topic="'"+jole[1]+"'"
    graphe=GraphDatabase.driver("bolt://18.221.34.104/:7687",auth=("neo4j","mathers22"))
    sess=graphe.session()
    print("working")
    print(topic)
    query="UNWIND $mer_list as row MATCH(m:topic{name:"+topic+"}) CREATE(n:video{name:row.degree,topic:row.topic,id:row.video_id,img:row.img,title:row.title})-[:VIDEO_OF]->(m)"
    sess.run(query,mer_list=mer_list)
    print("worked")
def main():
    print("dope")
if __name__ == '__main__':
    main()