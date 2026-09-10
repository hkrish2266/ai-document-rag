from flask import Flask, jsonify, request
from flask_cors import CORS
from pypdf import PdfReader
import io

from services.text_chunker import split_text
from services.rag import (
    create_vector_store,
    search_similar_chunks
)
from services.llm import generate_answer


app = Flask(__name__)
CORS(app)


# Stores the currently uploaded document
vector_store = []
document_name = ""
chat_history = []

@app.route("/")
def home():
    return jsonify({
        "message": "AI Document RAG backend is running!"
    })


@app.route("/api/health")
def health():
    return jsonify({
        "status": "success",
        "message": "Backend connection is working!"
    })


@app.route("/api/upload", methods=["POST"])
def upload_document():

    global vector_store
    global document_name
    global chat_history

    if "file" not in request.files:
        return jsonify({
            "status": "error",
            "message": "No file uploaded."
        }), 400

    file = request.files["file"]

    if file.filename == "":
        return jsonify({
            "status": "error",
            "message": "No file selected."
        }), 400

    if not file.filename.lower().endswith(".pdf"):
        return jsonify({
            "status": "error",
            "message": "Only PDF files are supported."
        }), 400

    try:

        file_data = file.read()

        reader = PdfReader(
            io.BytesIO(file_data)
        )

        text = ""

        for page in reader.pages:

            page_text = page.extract_text()

            if page_text:
                text += page_text + "\n"

        if not text.strip():
            return jsonify({
                "status": "error",
                "message": "Could not extract text from this PDF."
            }), 400

        # Split document into chunks
        chunks = split_text(text)

        if not chunks:
            return jsonify({
                "status": "error",
                "message": "Could not create document chunks."
            }), 400

        # Create embeddings and vector store
        vector_store = create_vector_store(chunks)

        document_name = file.filename
        chat_history = []

        return jsonify({
            "status": "success",
            "filename": file.filename,
            "pages": len(reader.pages),
            "chunk_count": len(chunks),
            "message": "Document uploaded and processed successfully."
        })

    except Exception as error:

        return jsonify({
            "status": "error",
            "message": f"Error processing PDF: {str(error)}"
        }), 500


@app.route("/api/ask", methods=["POST"])
def ask_question():

    global chat_history

    if not vector_store:
        return jsonify({
            "status": "error",
            "message": "Please upload a PDF first."
        }), 400

    data = request.get_json(silent=True)

    if not data:
        return jsonify({
            "status": "error",
            "message": "Request body is required."
        }), 400

    question = data.get("question", "").strip()

    if not question:
        return jsonify({
            "status": "error",
            "message": "Please enter a question."
        }), 400

    try:

        # Find relevant document chunks
        results = search_similar_chunks(
            question,
            vector_store,
            top_k=3
        )

        # Generate answer
        answer = generate_answer(
            question,
            results
        )

        # Save conversation
        chat_history.append({
            "question": question,
            "answer": answer
        })

        sources = []

        for result in results:

            sources.append({
                "chunk_id": result["id"],
                "score": round(result["score"], 4),
                "text": result["text"]
            })

        return jsonify({
            "status": "success",
            "question": question,
            "answer": answer,
            "document": document_name,
            "sources": sources,
            "chat_history": chat_history
        })

    except Exception as error:

        return jsonify({
            "status": "error",
            "message": f"Error answering question: {str(error)}"
        }), 500


if __name__ == "__main__":
    app.run(
        host="127.0.0.1",
        port=5000,
        debug=True
    )
