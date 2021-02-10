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



def jeb(jolt):
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
    
    jole=jolt.split(",")
    subject=jole[0]
    topic=jole[1]
    
    
    url="https://www.youtube.com/results?search_query="+topic+"in="+subject
    driver.get(url)
    try:
        element =WebDriverWait(driver,10).until(
        EC.presence_of_all_elements_located((By.ID,"dismissable"))
        )
       
        
        # element.click()
        # elemente =WebDriverWait(driver,10).until(
        # EC.presence_of_all_elements_located((By.TAG_NAME,"b"))
        # )
        youtube_data=[]
        for i in range(len(element)):
            apii=element[i].find_element_by_id("thumbnail").get_attribute("href"),element[i].find_element_by_id("img").get_attribute("src"),element[i].find_element_by_tag_name("yt-formatted-string").get_attribute("aria-label")
            youtube_data.append(apii)
        print(youtube_data)
        # print(element[0].find_element_by_id("img").get_attribute("src"))
        # print(element[0].find_element_by_tag_name("yt-formatted-string").get_attribute("aria-label"))
        # # ans=element.get_attribute('innerText').split()
       
        # if(ans[0]=="2" or ans[0]=="1"):
        #     jolt[1][topic]=ans[0]
        
        
        
    finally:
        driver.quit()
def main():
    jeb("number+theory,rsa")
if __name__ == '__main__':
    main()