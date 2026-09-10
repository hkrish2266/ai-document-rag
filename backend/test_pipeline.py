from services.rag import (
    create_vector_store,
    search_similar_chunks
)

from services.llm import generate_answer


# Sample document chunks
chunks = [
    "Amazon EC2 provides virtual servers in the cloud.",
    "Amazon S3 is an object storage service used to store files.",
    "Amazon DynamoDB is a managed NoSQL database.",
    "AWS Lambda runs code without managing servers."
]


# Create vector store
vector_store = create_vector_store(chunks)


# User question
question = "What is Amazon EC2?"


# Retrieve relevant chunks
results = search_similar_chunks(
    question,
    vector_store,
    top_k=2
)


# Generate answer
answer = generate_answer(
    question,
    results
)


print("Question:")
print(question)

print("\nAnswer:")
print(answer)

print("\nSources:")

for result in results:
    print(
        f"- Chunk {result['id']} "
        f"(score: {result['score']:.4f})"
    )
