import os
import glob
import re
from qdrant_client import QdrantClient
from qdrant_client.http import models
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv(dotenv_path='server/.env')

REQUIRED_ENV_VARS = ["OPENAI_API_KEY", "QDRANT_URL", "QDRANT_API_KEY"]
missing_vars = [var for var in REQUIRED_ENV_VARS if not os.getenv(var)]
if missing_vars:
    print(f"❌ Missing required environment variables: {', '.join(missing_vars)}")
    print("Please ensure they are set in server/.env or your system environment.")
    exit(1)

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
qdrant = QdrantClient(url=os.getenv("QDRANT_URL"), api_key=os.getenv("QDRANT_API_KEY"))

COLLECTION_NAME = "physical_ai_textbook"

def get_embedding(text, model="text-embedding-3-small"):
    text = text.replace("\n", " ")
    return client.embeddings.create(input=[text], model=model).data[0].embedding

def parse_mdx(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Simple chunking by heading (## or ###)
    chunks = re.split(r'\n(##+ .*)\n', content)
    
    doc_id = os.path.basename(file_path).replace('.mdx', '').replace('.md', '')
    
    processed_chunks = []
    current_header = "Introduction"
    
    for i in range(len(chunks)):
        if i == 0:
            if chunks[i].strip():
                processed_chunks.append({
                    "text": chunks[i].strip(),
                    "header": current_header,
                    "doc_id": doc_id
                })
        elif i % 2 == 1:
            current_header = chunks[i].strip('# ')
        else:
            if chunks[i].strip():
                processed_chunks.append({
                    "text": chunks[i].strip(),
                    "header": current_header,
                    "doc_id": doc_id
                })
    
    return processed_chunks

def initialize_collection():
    try:
        qdrant.create_collection(
            collection_name=COLLECTION_NAME,
            vectors_config=models.VectorParams(size=1536, distance=models.Distance.COSINE),
        )
        print(f"Collection {COLLECTION_NAME} created.")
    except Exception as e:
        print(f"Collection might already exist: {e}")

def ingest_all_content():
    initialize_collection()
    
    docs_path = 'docs/**/*.md*'
    files = glob.glob(docs_path, recursive=True)
    
    points = []
    idx = 0
    
    for file in files:
        if 'node_modules' in file or '_templates' in file:
            continue
            
        print(f"Processing {file}...")
        chunks = parse_mdx(file)
        
        for chunk in chunks:
            vector = get_embedding(chunk['text'])
            points.append(models.PointStruct(
                id=idx,
                vector=vector,
                payload={
                    "text": chunk['text'],
                    "header": chunk['header'],
                    "doc_id": chunk['doc_id'],
                    "source": file
                }
            ))
            idx += 1
            
    if points:
        qdrant.upsert(
            collection_name=COLLECTION_NAME,
            points=points
        )
        print(f"✅ Ingested {idx} chunks into Qdrant.")

if __name__ == "__main__":
    ingest_all_content()
