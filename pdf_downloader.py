from neo4j import GraphDatabase

graphe=GraphDatabase.driver(uri="bolt://localhost:7687",auth=("neo4j","mathers22"))
e=["1", "2", "3", "4", "5", "6", "7"]
def connect(subject,data_list):

    session=graphe.session()
    
    query="CREATE(:subject{name:$subjec})"
    
    session.run(query,subjec=subject,data=data_list)
    match="blot"

    for i in range(len(data_list)):
        query +=","+"(:topic{name:"+str(data_list[i])+",subject:$match_query})"
        print (query)
    print(query)

    nodes=session.run(query,subjec=subject,match_query=match)
    print("solider")
   
connect("debby",e)