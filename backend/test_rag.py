from services.rag import (
    create_vector_store,
    search_similar_chunks
)


chunks = [
    "Amazon EC2 provides virtual servers in the cloud.",
    "Amazon S3 is an object storage service.",
    "Amazon DynamoDB is a managed NoSQL database.",
    "AWS Lambda runs code without managing servers."
]


vector_store = create_vector_store(chunks)

question = "What is Amazon EC2?"

results = search_similar_chunks(
    question,
    vector_store,
    top_k=2
)


print("Question:")
print(question)

print("\nMost relevant chunks:")

for result in results:

    print("\nScore:", round(result["score"], 4))
    print("Text:", result["text"])
