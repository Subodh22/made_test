import urllib.request
import re 
html = urllib.request.urlopen("https://www.youtube.com/results?search_query=rsa+algorithm+in+number+theory")

video_ids = re.findall(r"watch\?v=(\S{11})",html.read().decode())

print(str(video_ids))
print("https://www.youtube.com/watch?v="+video_ids[0])