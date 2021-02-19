import json

with open('./major_json/Electrical Engineering and Computer Science (Course 6).json','r') as college_data:
    majors = json.load(college_data)
print(len(majors))
