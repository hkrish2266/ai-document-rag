from services.llm import generate_answer


question = "What is Amazon EC2?"

context = [
    {
        "id": 0,
        "text": "Amazon EC2 provides virtual servers in the cloud.",
        "score": 0.95
    },
    {
        "id": 1,
        "text": "Amazon S3 is an object storage service.",
        "score": 0.40
    }
]


answer = generate_answer(
    question,
    context
)


print("Question:")
print(question)

print("\nAI Answer:")
print(answer)