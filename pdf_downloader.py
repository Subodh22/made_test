from neo4j import GraphDatabase
import py2neo
import urllib.request
import re 
from youtube_api import jeb
from googleapiclient.discovery import build
api_key = "AIzaSyCaa-dKG3l0I4Uu-LyCH_qP611lRUl2THY"
 
service = build('youtube','v3',developerKey=api_key)


class dog:

    def __init__(self, uri, user, password):
            self._driver = GraphDatabase.driver(uri, auth=(user, password))

    def add_person(self, subject,data_list):
        with self._driver.session() as session:
            session.write_transaction(self.create_obj, subject,data_list)
            session.write_transaction(self.match_connect, subject)
            session.write_transaction(self.topic_degree, subject,data_list)
            # session.write_transaction(self.video_connect, subject,data_list)
            # session.read_transaction(self.check)
            print("running")
    @staticmethod
    def check(tx):
        q1="MATCH()-[r:AHEAD_OF]->() return count(*)"
        nodes=tx.run(q1)
        print(nodes)
        

    @staticmethod
    def create_obj(tx,subject,data_list):
        subject
        query="CREATE(:subject{name:$subjec})"
        
        for i in range(len(data_list)):
            print(i)
            genny="'"+str(data_list[i])+"'"
            gon="'"+str(i)+"'"
            query +=","+"(:topic{name:"+genny+",subject:$match_query,degree:"+gon+"})"
        print(query)
        tx.run(query,subjec=subject,match_query=subject)
    @staticmethod
    def match_connect(tx,subject):
        match_querye="MATCH(x:topic{subject:$subjec}),(y:subject{name:$subjec})CREATE (x)-[:TOPIC_OF]->(y)"
        tx.run(match_querye,subjec=subject)
        

    @staticmethod
    def topic_degree(tx,subject,data_list):
        degree_query=""
        degre_match="MATCH"
        degre_create="CREATE"
        for i in range(len(data_list)):
           jerry=","
           j="x"+str(i)
           z="x"+str(i+1)
           jolly="'"+str(data_list[i])+"'"
           if(i+1==len(data_list)):
               jerry=" "
               degre_create=degre_create[:-1]
           else:
               degre_create +=" " +"("+j+")-[:AHEAD_OF]->("+z+")"+jerry

           degre_match +=" "+"("+j+":topic{name:"+jolly+",subject:$subjec})"+jerry
        degree_query=degre_match+degre_create 
        print(degree_query)
        tx.run(degree_query,subjec=subject)

    
            

    # def jun(items):
        # query="UNWIND $mer_list as row MATCH(m:topic{name:"+filter_data+"}) CREATE(n:video{name:row.degree,topic:row.topic,id:row.id,img:row.img,title:row.title,des:row.des,duration:row.duration,views:row.view_count})-[:VIDEO_OF]->(m)"
        #     tx.run(query,mer_list=mer_list)




