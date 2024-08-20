# Bu kod kullanıcıların doğal dilde sorgular sormasını ve bu sorguların GPT-4 tarafından Cypher sorgularına dönüştürülmesini sağlar. Daha sonra Cypher sorgusu Neo4j veritabanında çalıştırılır ve sonuçlar kullanıcıya sunulur. 

# import os # İşletim sistemi ile etkileşime geçmeyi sağlar. Çevresel değişkenleri alarak OpenAI api anahtarını yönetir, dosya ve dizin işlemleri yapabilir.
import os
import openai # GPT-4 modeli ile metin üretimi ve sorgu oluşturma işlemleri yapar.
import streamlit as st
from streamlit_chat import message # Kullanıcı ve asistan arasındaki mesajları görselleştirir.
from driver import read_query # Oluşturulan Cypher sorgusunu Neo4j veritabanında çalıştırmak ve sonuçları okumak için kullanılır.
from train_cypher import examples # Çeşitli örnek Cypher sorgularını içerir ve GPT-4'ün Cypher sorguları oluşturmasını sağlamak için kullanılır.
from openaigpt4 import generate_cypher # Kullanıcı tarafından girilen doğal dil sorgularını alır ve GPT-4 kullanarak Cypher sorgularına dönüştürür.

# Streamlit uygulamasının sayfa yapılandırmasını ayarlar. page_title web tarayıcısının sekme başlığını ayarlar.
# Streamlit uygulamasının sayfasında büyük ve belirgin bir başlık oluşturulur.
# st.info sayfada bilgi içeren bir kutu oluşturur.

st.set_page_config(page_title="💬 Ask Me, Rahul")
st.title("💬 Ask Me, Rahul ")
st.info("Ask me V0.01 - Rahul | Powered By GPT-4",icon="ℹ️")

openai.api_key = "sk-proj-CjCrQtfnzXk6DJdWlB6lT3BlbkFJ5g9P1a0uUZQEb284IFnB"


# Bu kod kullanıcıdan gelen bir metni (prompt) işleyerek bir Cypher sorgusu üretir ve bu sorguyu çalıştırarak bir yanıt döner. 
    # cypher parametresi fonksiyonun bir Cypher sorgusu oluşturup oluşturmayacağını belirler.
    # Kullanıcının girdiği hazırlanır. 
    # generate_cypher, usr_input listesi kullanılarak cypher sorgusu oluşturulur.
    # read_guery, cypher_query değişkeni kullanılarak neo4j'ye sorgu gönderir ve sonucu alır.
    # Yanıt ve sorgu döndürülür.

def generate_response(prompt, cypher=True):
    usr_input = [{"role": "user", "content": prompt}]
    cypher_query = generate_cypher(usr_input)
    response_message = read_query(cypher_query)
    return response_message, cypher_query

with st.sidebar:
    st.markdown('📖 Learn more about-Me')
    
if "messages" not in st.session_state.keys():
    st.session_state.messages = [{"role": "assistant", "content": "How may I help you?"}]

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
            st.write(message["content"])

if user_input := st.chat_input():
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
            st.write(user_input)

# Son mesaj asistan tarafından girilmediyse kod çalışır. Asistanın mesajını görüntülemek için bir sohbet mesajı oluşur. Kullanıcı girdisine göre bir yanıt ve ilgili cypher sorgusu oluşur. Yanıt mesajını message içine uygun formatta atar. Oluşturulan cypher sorgusunda MATCH varsa kod çalışır. Amaç veri tabanından veri çekmek olan sorgular için kodun geçerli olmasıdır. Cypher sorgusu ekranda yazdırılır. Asistan yanıtının içeriği yazdırılır. 

if st.session_state.messages[-1]["role"] != "assistant":
    with st.chat_message("assistant"):
        response,cypher_query = generate_response(user_input) 
        message = {"role": "assistant", "content": response}
        if "MATCH" in cypher_query:
            st.write(cypher_query)
        st.write(message["content"]) 
        st.session_state.messages.append(message)


# Neo4j sonuçları genellikle bir liste içinde döndürülür ve her sonuç bir indeks ile birlikte gösterilir.