import os
from typing import List, Dict, Any
from openai import AsyncOpenAI
from qdrant_client import QdrantClient
from qdrant_client.http import models

class PhysicalAIAgent:
    def __init__(self):
        self.openai_client = AsyncOpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        self.qdrant_client = QdrantClient(
            url=os.getenv("QDRANT_URL"), 
            api_key=os.getenv("QDRANT_API_KEY")
        )
        self.collection_name = "physical_ai_textbook"
        self.model = "gpt-4o-mini"
        self.embedding_model = "text-embedding-3-small"

    async def get_embedding(self, text: str) -> List[float]:
        text = text.replace("\n", " ")
        response = await self.openai_client.embeddings.create(input=[text], model=self.embedding_model)
        return response.data[0].embedding

    async def search_context(self, query: str, limit: int = 5) -> List[Dict[str, Any]]:
        vector = await self.get_embedding(query)
        search_result = self.qdrant_client.search(
            collection_name=self.collection_name,
            query_vector=vector,
            limit=limit
        )
        return [
            {
                "text": hit.payload["text"],
                "header": hit.payload["header"],
                "doc_id": hit.payload["doc_id"],
                "source": hit.payload["source"]
            }
            for hit in search_result
        ]

    async def generate_response(self, message: str, history: List[Dict[str, str]] = []) -> Dict[str, Any]:
        try:
            context_items = await self.search_context(message)
        except Exception:
            context_items = []
            
        context_text = "\n\n".join([f"Source: {c['doc_id']} > {c['header']}\nContent: {c['text']}" for c in context_items])
        
        system_prompt = f"""You are the Physical AI & Humanoid Robotics Textbook Assistant. 
Your goal is to help students understand the textbook content.
Use the provided context to answer the question. If the answer isn't in the context, say you don't know based on the textbook but offer general knowledge if appropriate, while clearly stating it's not from the book.
Always provide citations in the format [doc_id].

Context:
{context_text}
"""
        
        messages = [{"role": "system", "content": system_prompt}]
        messages.extend(history)
        messages.append({"role": "user", "content": message})
        
        response = await self.openai_client.chat.completions.create(
            model=self.model,
            messages=messages,
            temperature=0.7
        )
        
        answer = response.choices[0].message.content
        citations = list(set([c['doc_id'] for c in context_items]))
        
        return {
            "answer": answer,
            "citations": citations
        }
