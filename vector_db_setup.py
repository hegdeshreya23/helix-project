import os
from pinecone import Pinecone, ServerlessSpec
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def init_pinecone():
    # Initialize Pinecone with new syntax
    pc = Pinecone(
        api_key=os.getenv('PINECONE_API_KEY')
    )
    
    # Create index if it doesn't exist
    index_name = "helix"
    
    # Check if index already exists
    if index_name not in pc.list_indexes().names():
        # Create new index with serverless spec
        pc.create_index(
            name=index_name,
            dimension=1536,  # dimension for text-embedding-3-small
            metric='cosine',
            spec=ServerlessSpec(
                cloud='aws',
                region='us-east-1'
            )
        )
        print(f"Created new index: {index_name}")
    else:
        print(f"Index {index_name} already exists")
    
    # Connect to index
    index = pc.Index(index_name)
    return index

if __name__ == "__main__":
    try:
        index = init_pinecone()
        print("Pinecone initialization successful!")
        
        # Test the index with a simple query
        stats = index.describe_index_stats()
        print(f"Index stats: {stats}")
        
    except Exception as e:
        print(f"Error initializing Pinecone: {e}")