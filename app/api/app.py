
from llama_index.llms.cohere import Cohere
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, ServiceContext
from llama_index.embeddings.cohere import CohereEmbedding
from llama_index.postprocessor.cohere_rerank import CohereRerank
from llama_index.core.memory import ChatMemoryBuffer
from os.path import dirname, abspath, join

from flask import Flask
from flask import request
import os

dir = dirname(abspath(__file__))
API_KEY = os.environ['COHERE_API']
# Create the embedding model
embed_model = CohereEmbedding(
    cohere_api_key=API_KEY,
    model_name="embed-english-v3.0",
    input_type="search_query",
)

# Create the service context with the cohere model for generation and embedding model
service_context = ServiceContext.from_defaults(
    llm=Cohere(api_key=API_KEY, model="command"),
    embed_model=embed_model
)
# Load the data, for this example data needs to be in a test file 
#data = SimpleDirectoryReader(input_dir="data",input_files=["test.pdf"]).load_data()
data = SimpleDirectoryReader(input_files=["test.pdf"]).load_data()
index = VectorStoreIndex.from_documents(data, service_context=service_context)

# Create a cohere reranker 
cohere_rerank = CohereRerank(api_key=API_KEY)


memory = ChatMemoryBuffer.from_defaults(token_limit=1500)

chat_engine = index.as_chat_engine(
    chat_mode="context",
    memory=memory,
    system_prompt=(
        "You are a chatbot, able to have normal interactions, as well as talk"
        " about a prospective candidate for hire."
    ),
    node_postprocessors=[cohere_rerank]
)

 
app = Flask(__name__)

@app.route("/api/chat")
def hello_world():
    question= request.args.get('question')
    question = "Hello! !" if question is None else question
    response = chat_engine.chat(question)
    return str(response)