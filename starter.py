import os
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader
os.environ['OPENAI_API_KEY'] = 'sk-****'
# os.environ['HTTPS_PROXY'] = "http://{}".format("127.0.0.1:7890")

documents = SimpleDirectoryReader("data").load_data()
index = VectorStoreIndex.from_documents(documents)

query_engine = index.as_query_engine()
response = query_engine.query("What did the author do growing up?")
print(response)
print('\n')

response = query_engine.query("Who is the author?")
print(response)
print('\n')

response = query_engine.query("Introduce me Paul Graham")
print(response)