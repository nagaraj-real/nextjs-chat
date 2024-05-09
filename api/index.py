from pprint import pprint
from flask import Flask,request
from langchain_cohere import ChatCohere,CohereRagRetriever
from langchain_community.document_loaders import PyPDFLoader
import os

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

