from neo4j import GraphDatabase

BATCH = {'batch': []}
# query = "UNWIND $batch AS row MERGE (y:User{name:row['name']}) MERGE (y)-[:AHEAD_OF]->(e:User{id:row['ahead_of']}) "
BATCH["batch"] =  [{"id": "x1", "name": "Toto","subject":"math","ahead_of":"x2"},{"id":"x2","name":"tome","subject":"math","ahead_of":""}]
query="UNWIND $batch as row CREATE (x:user{id:row['id'],name:row['name],'ahead_of':"str(row['ahead_of'])"})"
graphe=GraphDatabase.driver("bolt://localhost:7687",auth=("neo4j","mathers22"))
session=graphe.session()
session.run(query,batch=BATCH["batch"])