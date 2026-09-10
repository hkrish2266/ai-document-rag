import hashlib
import math


def create_embedding(text, dimensions=128):
    """
    Create a deterministic lightweight embedding for local testing.

    This is NOT the final AI embedding model.
    It allows us to test the RAG pipeline without
    requiring AWS credentials during development.
    """

    if not text or not text.strip():
        return []

    vector = [0.0] * dimensions

    words = text.lower().split()

    for word in words:

        # Create a stable number from the word
        hash_bytes = hashlib.sha256(
            word.encode("utf-8")
        ).digest()

        number = int.from_bytes(
            hash_bytes[:4],
            byteorder="big"
        )

        index = number % dimensions

        vector[index] += 1.0

    # Normalize the vector
    magnitude = math.sqrt(
        sum(value * value for value in vector)
    )

    if magnitude == 0:
        return vector

    return [
        value / magnitude
        for value in vector
    ]
