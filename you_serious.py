from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time



def jeber(jolt):
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
    
    
    subject=jolt[0]
    topic=jolt[1]
    
    print(jolt[3])
    url="https://www.sixdegreesofwikipedia.com/?source="+subject+"&target="+topic
    driver.get(url)
    try:
        element =WebDriverWait(driver,10).until(
        EC.presence_of_element_located((By.TAG_NAME,"button"))
        )
        element.click()
        print("working")
        elemente =WebDriverWait(driver,10).until(
        EC.presence_of_all_elements_located((By.TAG_NAME,"b"))
        )
        print(elemente)
        
       
        ans=elemente[len(elemente)-2].get_attribute('innerText').split()
    
        print(ans)
        print("working")
       
        if(ans[0]=="2" or ans[0]=="1"or ans[0]=="0"):
            
            jolt[2][jolt[3]]=topic
            
            print(jolt[1])
       
        
        
    finally:
        driver.quit()
def main():
    print("sele_herer")
if __name__ == '__main__':
    main()

