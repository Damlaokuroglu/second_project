# Bu kod Neo4j veritabanı şemasına dayalı olarak Cypher sorguları oluşturabilen bir asistan yaratmayı amaçlar. Şema ve örnek Cypher sorguları ile birlikte asistanın görev tanımını belirler. 

# Örnek cypher sorgularını içeren modülden kodda kullanılacak cypher sorguları alınır.

from train_cypher import examples, node_properties, relationships_props

# Bu kod Neo4j veritabanı şemasının bir metin temsilini oluşturur. Düğüm ve ilişkiler hakkında bilgi alır ve bilgileri birleştirerek formatlanmış bir metin döner. node_props düğüm özelliklerinin tanımını içeren bir parametredir.

def get_schema_text(node_props, rels):
    return f"""
  This is the schema representation of the Neo4j database.
  Node properties are the following:
  {node_props}
  Relationships from source to target nodes:
  {rels}
  Make sure to respect relationship types and directions
  """

# schema_text = get_schema_text(node_properties, relationships_props)
# print(schema_text)

# Neo4j veritabanında sorgular oluşturmak için asistanın ne yapacağını ve nasıl yapacağını belirler. Sistem talimatlarını ve şema bilgisini içeren bir mesaj oluşur. Task, görevin sağlanan şema tanımına dayanarak Neo4j grafik veritabanı için Cypher sorguları oluşturmak olduğunu belirtir. 

def get_system_message(schema_text):
    return f"""
        You are an assistant with an ability to generate Cypher queries.
        Task: Generate Cypher queries to query a Neo4j graph database based on the provided schema definition.
        Instructions:
        Use only the provided relationship types.
        Do not use any other relationship types or properties that are not provided.
        If you cannot generate a Cypher statement based on the provided schema, explain the reason to the user.
        Schema:
        {schema_text}
        Example cypher queries are:
        {examples}
        """

# schema_text = get_schema_text(node_properties, relationships_props)
# system_message = get_system_message(schema_text)
# print(system_message)

# Bu kod Neo4j veritabanı şemasının bir temsilini döndüren bir fonksiyon tanımlar. Neo4j veritabanı şemasının metadata'sını almak için bir fonksiyon oluşturulur. get_schema_text fonksiyonuna gerekli bilgiler sağlanarak şema bilgilerini içeren bir metin döndürülür. 

def get_graph_model_metadata():
    return get_schema_text(node_props=node_properties,rels=relationships_props)

# schema_metadata = get_graph_model_metadata()
# print(schema_metadata)

# İki fonksiyonu biraraya getirerek bir sistem mesajı oluşturur. get_graph_model_metadata fonksiyonu çağrılarak dönen değer schema_txt değişkenine atılır. get_graph_model_metadata fonksiyonu get_schema_text fonksiyonunu çağırır ve node_properties ile relationships_props değişkenlerini kullanarak(şema metnini kullanarak) asistana yönelik bir sistem mesajı oluşturur. Bu fonksiyon veritabanı şemasının ayrıntılı bir açıklamasını sağlar. get_sys_prompts fonksiyonu oluşan sistem mesajını döndürür. 

def get_sys_prompts():
    schema_txt = get_graph_model_metadata()
    return get_system_message(schema_txt)

# sys_prompts = get_sys_prompts()
# print(sys_prompts) # diğer kodlarda adım adım yaptığımızı tüm işlemleri biraraya getirip yaptık. 
