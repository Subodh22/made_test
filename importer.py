from neo4j import GraphDatabase

graphe=GraphDatabase.driver("bolt://localhost/:7687",auth=("neo4j","mathers22"))
sess=graphe.session()


query="""CREATE (x:name{name:"jone",july:"buzzvut"})"""
sess.run(query)
sess.close()
