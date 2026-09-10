import math

from services.embeddings import create_embedding


def cosine_similarity(vector_a, vector_b):
    """Calculate cosine similarity between two vectors."""

    if not vector_a or not vector_b:
        return 0.0

    if len(vector_a) != len(vector_b):
        return 0.0

    dot_product = sum(
        a * b
        for a, b in zip(vector_a, vector_b)
    )

    magnitude_a = math.sqrt(
        sum(a * a for a in vector_a)
    )

    magnitude_b = math.sqrt(
        sum(b * b for b in vector_b)
    )

    if magnitude_a == 0 or magnitude_b == 0:
        return 0.0

    return dot_product / (magnitude_a * magnitude_b)


def create_vector_store(chunks):
    """Create embeddings for all document chunks."""

    vector_store = []

    for index, chunk in enumerate(chunks):

        embedding = create_embedding(chunk)

        vector_store.append({
            "id": index,
            "text": chunk,
            "embedding": embedding
        })

    return vector_store


def search_similar_chunks(
    question,
    vector_store,
    top_k=3
):
    """Find the most relevant chunks for a question."""

    if not question.strip():
        return []

    if not vector_store:
        return []

    question_embedding = create_embedding(question)

    results = []

    for item in vector_store:

        score = cosine_similarity(
            question_embedding,
            item["embedding"]
        )

        results.append({
            "id": item["id"],
            "text": item["text"],
            "score": score
        })

    results.sort(
        key=lambda item: item["score"],
        reverse=True
    )

    return results[:top_k]