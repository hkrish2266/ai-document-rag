def build_rag_prompt(question, context):
    """
    Build a prompt that instructs an LLM to answer
    using only the retrieved document information.
    """

    if not context:
        return (
            "You are a helpful document assistant.\n"
            "No relevant document information was found."
        )

    context_text = "\n\n".join(
        item["text"]
        for item in context
    )

    return f"""
You are an AI document assistant.

Answer the user's question using ONLY the
information in the document context.

Rules:
1. Do not invent information.
2. Do not use outside knowledge.
3. If the answer is not in the context,
   say that you could not find the answer
   in the document.
4. Keep the answer clear and concise.

DOCUMENT CONTEXT:
-----------------
{context_text}
-----------------

USER QUESTION:
{question}

ANSWER:
""".strip()
