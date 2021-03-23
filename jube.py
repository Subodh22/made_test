import json
def openJson(name_tag):
    pathe='./amc/'+name_tag+'.json'
    with open(pathe,'r') as college_data:
      majors = json.load(college_data)
      
      if majors!=[] :
            print("bonkers")
openJson('15.0341 Econometrics for Managers: Correlation and Causality in a Big Data World')