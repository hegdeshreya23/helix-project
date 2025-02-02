import os
import uuid
from pinecone import Pinecone
import openai
from dotenv import load_dotenv

load_dotenv()

class VectorManager:
    def __init__(self):
        # Initialize OpenAI
        openai.api_key = os.getenv('OPENAI_API_KEY')
        
        # Initialize Pinecone with new syntax
        pc = Pinecone(
            api_key=os.getenv('PINECONE_API_KEY')
        )
        
        self.index = pc.Index("helix")
    
    def get_embedding(self, text):
        """Generate embedding for text using OpenAI"""
        response = openai.embeddings.create(
            model="text-embedding-3-small",
            input=text
        )
        return response.data[0].embedding
    
    def store_embedding(self, text, metadata=None):
        """Store text embedding with metadata"""
        embedding = self.get_embedding(text)
        
        # Generate a unique ID for the vector
        vector_id = str(uuid.uuid4())
        
        # Store in Pinecone
        self.index.upsert(
            vectors=[(vector_id, embedding, metadata)]
        )
        
        return vector_id
    
    def search_similar(self, text, top_k=5):
        """Search for similar texts"""
        query_embedding = self.get_embedding(text)
        
        # Search in Pinecone
        results = self.index.query(
            vector=query_embedding,
            top_k=top_k,
            include_metadata=True
        )
        
        return results