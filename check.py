import os
from dotenv import load_dotenv
from langchain_community.document_loaders import PDFPlumberLoader
from langchain_experimental.text_splitter import SemanticChunker
from langchain_google_vertexai import VertexAIEmbeddings
from google.cloud import aiplatform
from google.oauth2 import service_account
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import PGVector
import psycopg
import pprint
import re
load_dotenv(dotenv_path='./.env')
credent = service_account.Credentials.from_service_account_file(os.environ.get("GOOGLE_APPLICATION_CREDENTIALS"))

aiplatform.init(project='vertex-test-450206',location='us-central1',credentials=credent)
embeddingmodel=VertexAIEmbeddings(model_name='text-embedding-005')

pdfpaths=["How to Sleep Better-Harvard Health.pdf"]
loader=PDFPlumberLoader(pdfpaths[0])
document=loader.load()
def clean_texts(texts):
    url_pattern = re.compile(r'http\S+')
    timestamp_pattern = re.compile(r'\d{1,2}/\d{1,2}/\d{2,4}, \d{1,2}:\d{2} [APM]{2}')    
    related_articles_pattern = re.compile(r'Related Articles.*', re.IGNORECASE)
    cleaned_texts = []
    for text in texts: 
        cleaned_text = url_pattern.sub('', text) 
        cleaned_text = timestamp_pattern.sub('', cleaned_text) 
        cleaned_text = related_articles_pattern.sub('',cleaned_text)
        cleaned_texts.append(cleaned_text.strip()) 
    return cleaned_texts

text_splitter=RecursiveCharacterTextSplitter(chunk_size=1000,chunk_overlap=200)
text_chunks=text_splitter.create_documents([page.page_content for page in document])

cleaned_text=clean_texts(document[0].page_content)
final_chunks = text_splitter.create_documents(cleaned_text)
print(final_chunks)
# text_data = [chunk.page_content for chunk in text_chunks]
# processedtext=clean_texts(text_data)
# final_chunks=text_splitter.create_documents([text for text in processedtext])

# connectionurl=os.environ.get("CONNECTION_URL")
# collectionname="finaltest-vectors"

# db=PGVector.from_documents(embedding=embeddingmodel,documents=final_chunks,collection_name=collectionname,connection_string=connectionurl)
