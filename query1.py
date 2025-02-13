import os
from dotenv import load_dotenv
from langchain_community.document_loaders import PDFPlumberLoader
from langchain_experimental.text_splitter import SemanticChunker
from langchain_google_vertexai import VertexAIEmbeddings
from langchain_google_vertexai import ChatVertexAI
from google.cloud import aiplatform
from google.oauth2 import service_account
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import PGVector
from langchain.prompts import PromptTemplate
import psycopg
import pprint
import re

connectionurl=os.environ.get("CONNECTION_URL")
collectionname="finaltest-vectors"

database=PGVector(
    connection_string=os.environ.get("CONNECTION_URL"),
    collection_name="finaltest-vectors",
    embedding_function=VertexAIEmbeddings('text-embedding-005')
)



query = "How much deep sleep do i need to get, iam 21 years old"
retrieved_docs = database.similarity_search_with_score(query, k=3)

context = "\n\n".join([doc[0].page_content for doc in retrieved_docs])

medical_prompt = PromptTemplate(
    input_variables=["question", "context"],
    template=(
        "You are a medical professional providing detailed and accurate insights. "
        "Expand on the following question with a focus on scientific accuracy, "
        "clarity, and practical recommendations.\n\n"
        "Question: {question}\n\n"
        "Relevant medical context:\n{context}\n\n"
        "Provide a response that includes key details, potential concerns, and "
        "practical steps for better health outcomes."
    )
)


formatted_prompt = medical_prompt.format(question=query, context=context)


llm = ChatVertexAI(model_name="gemini-1.5-pro-002")


response = llm.invoke(formatted_prompt)
print(response)



