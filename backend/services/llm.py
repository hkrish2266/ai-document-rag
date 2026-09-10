import os

from dotenv import load_dotenv
from groq import Groq

from services.prompt import build_rag_prompt


load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    raise RuntimeError(
        "GROQ_API_KEY is not set. "
        "Check your .env file."
    )

client = Groq(
    api_key=api_key
)

MODEL = "openai/gpt-oss-20b"


def generate_answer(question, results):

    if not results:
        return "I could not find the answer in the document."

    context = build_rag_prompt(
        question,
        results
    )

    messages = [
        {
            "role": "system",
            "content": """
You are an AI document assistant.

Answer the user's question using ONLY
the provided document context.

Rules:
- Do not invent information.
- Do not use outside knowledge.
- If the answer is not present in the context, say:
  "I could not find this information in the provided document."
- Keep the answer clear and concise.
"""
        },
        {
            "role": "user",
            "content": context
        }
    ]

    try:
        response = client.chat.completions.create(
            model=MODEL,
            messages=messages,
            temperature=0
        )

        return response.choices[0].message.content.strip()

    except Exception as error:
        return (
            "Unable to generate an AI answer right now. "
            f"Groq error: {str(error)}"
        )


def create_llm_prompt(question, context):
    return build_rag_prompt(question, context)