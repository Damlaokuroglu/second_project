# Bu kod OpenAI'nin GPT-4 modelini kullanarak Neo4j grafik veritabanı için Cypher sorguları oluşturur. Önceki koddan farkı sistem mesajı ve şema metni doğrudan kodda bulunmuyor, ayrı fonksiyonlarla yönetiliyor. 

import openai
from train_cypher import node_properties,relationships_props
from train_utils import get_schema_text,get_system_message

def get_graph_model_metadata():
    return get_schema_text(node_props=node_properties,rels=relationships_props)

def get_sys_prompts():
    schema_txt = get_graph_model_metadata()
    return get_system_message(schema_txt)

# generate_cypher fonksiyonu messages adında bir listeyi kullanarak verilen mesajları baz alarak bir Cypher sorgusu üretmek için OpenAI GPT-4 modeline bir istek yapar. get_sys_prompts() fonksiyonu GPT modeline ne yapması gerektiğini açıklayan talimatları içeren sistem mesajını döndürür. messages içindeki liste sistem mesajını içerir. Gelen messages listesi sistem mesajından sonra eklenir. Böylece sistem mesajı ve kullanıcı tarafından sağlanan mesaj birleştirilir. openai.ChatCompletion.create OpenAI api'sine istek yapar, gönderilecek mesajlar belirlenir. completions nesnesinden api'den dönen ilk yanıt alınır ve response değişkenine atılır. response değeri döndürülür. Bu değer modelden alınan cypher kodudur.

def generate_cypher(messages):
    messages = [
        {"role": "system", "content": get_sys_prompts()}
    ] + messages
    # Make a request to OpenAI
    completions = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
        temperature=0.0
    )
    response = completions.choices[0].message["content"]
    return response

# example_messages = [
#     {"role": "user", "content": "Show part details for 19999?"}
# ]

# cypher_query = generate_cypher(example_messages)
# print(cypher_query)

# sys_prompts = get_sys_prompts()
# print(sys_prompts)

# response_content = completions.choices[0]['message']['content']
    # return response_content