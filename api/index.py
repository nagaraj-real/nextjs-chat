from pprint import pprint
from flask import Flask,request
from langchain_cohere import ChatCohere,CohereRagRetriever
from langchain_community.document_loaders import PyPDFLoader
import os
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

API_KEY = os.environ['COHERE_API_KEY']

def chat(user_query):
    llm = ChatCohere()
    rag = CohereRagRetriever(llm=llm, connectors=[])
    loader = PyPDFLoader('data/resum.pdf')
    docs = rag.get_relevant_documents(
        user_query,
        documents=loader.load(),
    )
    answer = docs.pop()
    return answer

app = Flask(__name__)
limiter = Limiter(
    get_remote_address,
    app=app,
    default_limits=["50 per day", "20 per hour"],
    storage_uri="memory://",
)

@app.route("/api/chat", methods = ['GET'])
def start_chat():
    question= request.args.get('question')
    question = "Hello! !" if question is None else question
    answer = chat(question)
    response= answer.page_content
    pprint("Answer:")
    pprint(answer.page_content)
    return str(response)

@app.route("/api/hello", methods = ['GET'])
def hello():
    return "hello"

