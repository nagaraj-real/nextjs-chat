from pprint import pprint
from flask import Flask,request
from langchain_cohere import ChatCohere, CohereEmbeddings, CohereRagRetriever, CohereRerank
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.vectorstores import Chroma
from langchain.retrievers import ContextualCompressionRetriever

import os

API_KEY = os.environ['COHERE_API']

def chat(user_query):
    # Create Cohere's chat model, embeddings and rerank objects.
    llm = ChatCohere(cohere_api_key=API_KEY)
    cohere_embeddings = CohereEmbeddings(cohere_api_key=API_KEY)
    cohere_rerank = CohereRerank(cohere_api_key=API_KEY)

    # Load text files and split into chunks, you can also use data gathered elsewhere in your application.
    loader = PyPDFLoader('data/resum.pdf')
    pages = loader.load_and_split()
    # Create a vector store from the documents
    chroma_index  = Chroma.from_documents(pages, cohere_embeddings)

    # Create Cohere's reranker with the vector DB using Cohere's embeddings as the base retriever.
    compression_retriever = ContextualCompressionRetriever(
        base_compressor=cohere_rerank,
        base_retriever=chroma_index.as_retriever()
    )
    compressed_docs = compression_retriever.get_relevant_documents(user_query)
    # Print the relevant documents from using the embeddings and reranker
    print(compressed_docs)

    # Create the cohere rag retriever using the chat model
    rag = CohereRagRetriever(llm=llm)
    docs = rag.get_relevant_documents(
        user_query,
        documents=compressed_docs,
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