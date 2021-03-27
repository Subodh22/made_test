import os 
import json

def openJson(name_tag):
    print(os.getcwd())
    
    pathe='./ad_sub/'+name_tag+'.json'
    with open(pathe,'r') as college_data:
      majors = json.load(college_data)
      print (majors)

openJson('Aerospace Engineering (Course 16)')