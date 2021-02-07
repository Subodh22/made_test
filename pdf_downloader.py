from neo4j import GraphDatabase
import py2neo


class dog:

    def __init__(self, uri, user, password):
            self._driver = GraphDatabase.driver(uri, auth=(user, password))

    def add_person(self, subject,data_list):
        with self._driver.session() as session:
            session.write_transaction(self.create_obj, subject,data_list)
            session.write_transaction(self.match_connect, subject)
            return session.write_transaction(self.topic_degree, subject,data_list)
    @staticmethod
    def create_obj(tx,subject,data_list):
        query="CREATE(:subject{name:$subjec})"
        
        for i in range(len(data_list)):
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
            
          
           
        print(degre_create)
        degree_query=str(degre_match)+str(degre_create)
       
        tx.run(degree_query,subjec=subject)



