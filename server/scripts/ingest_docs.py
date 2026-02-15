import os
import re
import uuid
import logging
from typing import List, Dict, Any
from pathlib import Path
from openai import OpenAI
from qdrant_client import QdrantClient
from qdrant_client.http import models
from dotenv import load_dotenv

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

load_dotenv()

class DocumentationIngestor:
    def __init__(self):
        self.openai_client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        self.qdrant_client = QdrantClient(
            url=os.getenv("QDRANT_URL"), 
            api_key=os.getenv("QDRANT_API_KEY")
        )
        self.collection_name = "physical_ai_textbook"
        self.embedding_model = "text-embedding-3-small"
        self.vector_size = 1536 # For text-embedding-3-small

    def get_embedding(self, text: str) -> List[float]:
        text = text.replace("\n", " ")
        return self.openai_client.embeddings.create(
            input=[text], 
            model=self.embedding_model
        ).data[0].embedding

    def init_collection(self):
        """Initialize the Qdrant collection if it doesn't exist."""
        collections = self.qdrant_client.get_collections().collections
        exists = any(c.name == self.collection_name for c in collections)
        
        if not exists:
            logger.info(f"Creating collection: {self.collection_name}")
            self.qdrant_client.create_collection(
                collection_name=self.collection_name,
                vectors_config=models.VectorParams(
                    size=self.vector_size,
                    distance=models.Distance.COSINE
                )
            )
        else:
            logger.info(f"Collection {self.collection_name} already exists.")

    def parse_mdx(self, file_path: Path) -> List[Dict[str, Any]]:
        """Parse MDX/MD files into chunks based on headers."""
        content = file_path.read_text(encoding='utf-8')
        doc_id = file_path.stem
        
        # Remove frontmatter
        content = re.sub(r'^---.*?---', '', content, flags=re.DOTALL)
        
        # Split by headers (h1, h2, h3)
        chunks = []
        current_header = "General"
        
        # Simple split by header lines
        sections = re.split(r'^(#+\s+.*)$', content, flags=re.MULTILINE)
        
        for i in range(1, len(sections), 2):
            header = sections[i].strip('#').strip()
            body = sections[i+1].strip() if i+1 < len(sections) else ""
            
            if len(body) > 50: # Only index substantial chunks
                chunks.append({
                    "doc_id": doc_id,
                    "header": header,
                    "text": body,
                    "source": str(file_path.relative_to(Path("D:/demo hackathon/Physical-AI-Humanoid-Robotics-Textbook/docs")))
                })
        
        return chunks

    def process_docs(self, docs_dir: str):
        """Walk through docs directory and ingest all markdown files."""
        self.init_collection()
        docs_path = Path(docs_dir)
        
        all_chunks = []
        for ext in ['*.md', '*.mdx']:
            for file_path in docs_path.rglob(ext):
                logger.info(f"Parsing {file_path}")
                try:
                    chunks = self.parse_mdx(file_path)
                    all_chunks.extend(chunks)
                except Exception as e:
                    logger.error(f"Failed to parse {file_path}: {e}")

        logger.info(f"Found {len(all_chunks)} chunks. Starting embedding and upsert...")
        
        points = []
        for chunk in all_chunks:
            vector = self.get_embedding(chunk['text'])
            points.append(models.PointStruct(
                id=str(uuid.uuid4()),
                vector=vector,
                payload=chunk
            ))
            
            # Batch upsert every 50 points
            if len(points) >= 50:
                self.qdrant_client.upsert(
                    collection_name=self.collection_name,
                    points=points
                )
                logger.info(f"Upserted {len(points)} points...")
                points = []
        
        # Final upsert
        if points:
            self.qdrant_client.upsert(
                collection_name=self.collection_name,
                points=points
            )
            logger.info(f"Final upsert completed.")

if __name__ == "__main__":
    ingestor = DocumentationIngestor()
    # Adjust path if necessary
    target_docs = "D:/demo hackathon/Physical-AI-Humanoid-Robotics-Textbook/docs"
    ingestor.process_docs(target_docs)
