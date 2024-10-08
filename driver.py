from neo4j import GraphDatabase

host = 'bolt://127.0.0.1:7687'
user = 'neo4j'
password = 'Damla1209'
driver = GraphDatabase.driver(host, auth=(user, password))

def read_query(query, params={}):
        with driver.session() as session:
            try:
                result = session.run(query, params)
                response = [r.values()[0] for r in result]
                if response == []:
                        return "Either there is no result found for your question Or please help me with additional context."
                return response
            except Exception as inst:
                if "MATCH" in query:
                    return "Either there is no result found for your question Or please help me with additional context!"
                else:
                    return query

# query = "MATCH (n) RETURN n LIMIT 2"
# params = {}

# result = read_query(query, params)
# print(result)
