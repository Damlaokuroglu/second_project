# Bu kod Neo4j veritabanı ile etkileşime geçer ve Cypher sorgularını çalıştırır. 

from neo4j import GraphDatabase # Neo4j veritabanına bağlanmak ve sorguları çalıştırmak için kullanılır.

# Driver nesnesi veritabanıyla etkileşimde bulunmak ve veritabanı işlemlerini gerçekleştirmek için bir arayüz sağlar. host bağlantı adresi bolt neo4j protokolüdür. driver nesnesi veritabanıyla etkileşime geçmek için oturumlar oluşturur. Bu oturumlar, sorguları çalıştırmak ve veritabanı işlemlerini gerçekleştirmek için kullanılır.

host = 'bolt://127.0.0.1:7687'
user = 'neo4j'
password = 'Damla1209'
driver = GraphDatabase.driver(host, auth=(user, password))

# Bu kod Neo4j veritabanından sorgu sonuçlarını almak için kullanılır. read_query cypher sorgusunu çalıştırır. driver.session() oturum başlatır. with  oturumun otomatik kapatılmasını sağlar. session.run() metodu sorguyu çalıştırır ve params ile sağlanan parametreler sorguya geçirilir. result sorgu sonuçlarını içerir. Sorgu sonuçlarından bir liste oluşturulur. Her sonucu (r) alır ve ilk değerini alarak response listesine ekler. r sorgu sonucunun her bir satırını temsil eder. values() r nesnesindeki tüm değerleri bir liste olarak döndürür, her bir sütun bir liste olarak döner. response listesi boşsa (yani sorgu sonuçsuzsa) kullanıcıya bir mesaj döndürür. Sorgu çalıştırılırken bir hata oluşursa bu hata yakalanır. Sorgu MATCH içeriyorsa özel bir mesaj döndürülür. Sorgu MATCH içermiyorsa sorgunun kendisi döndürülür.

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