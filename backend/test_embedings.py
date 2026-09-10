
from services.embeddings import create_embedding


text = "Amazon EC2 provides virtual servers in the cloud."

embedding = create_embedding(text)

print("Embedding created successfully.")
print("Vector length:", len(embedding))
print("First 10 values:", embedding[:10])
