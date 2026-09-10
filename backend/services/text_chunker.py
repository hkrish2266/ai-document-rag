def split_text(text, chunk_size=500, overlap=50):
    """
    Split text into smaller overlapping chunks.

    Args:
        text: The complete document text.
        chunk_size: Maximum number of characters in each chunk.
        overlap: Number of characters shared between chunks.

    Returns:
        A list of text chunks.
    """

    if not text or not text.strip():
        return []

    text = text.strip()

    if chunk_size <= 0:
        raise ValueError("chunk_size must be greater than 0")

    if overlap < 0 or overlap >= chunk_size:
        raise ValueError(
            "overlap must be >= 0 and smaller than chunk_size"
        )

    chunks = []

    start = 0
    text_length = len(text)

    while start < text_length:

        end = min(start + chunk_size, text_length)

        chunk = text[start:end].strip()

        if chunk:
            chunks.append(chunk)

        if end == text_length:
            break

        start = end - overlap

    return chunks