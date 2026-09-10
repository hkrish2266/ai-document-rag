# 🤖 AI Document RAG

An AI-powered **Retrieval-Augmented Generation (RAG)** application that allows users to upload PDF documents and ask questions about their content using **Amazon Bedrock**.

The application processes uploaded documents into searchable chunks, retrieves the most relevant information for a user's question, and uses an AI foundation model to generate a contextual answer.

---

## 📌 Overview

**AI Document RAG** combines document processing, semantic retrieval, and generative AI to create an interactive question-answering system for PDF documents.

Instead of asking an AI model to answer questions using only its general knowledge, the application first retrieves relevant information from the uploaded document and provides that information as context to the language model.

### Core workflow

```text
                 📄 PDF Document
                       │
                       ▼
                Text Extraction
                       │
                       ▼
                 Text Chunking
                       │
                       ▼
                  Embeddings
                       │
                       ▼
              🔎 Vector Retrieval
                       │
             Relevant Context
                       │
                       ▼
              🤖 Amazon Bedrock
                       │
                       ▼
                 AI Response
```

---

## ✨ Features

* 📄 Upload PDF documents
* 🔪 Split documents into manageable text chunks
* 🧠 Generate embeddings for document content
* 🔎 Retrieve relevant document context
* 🤖 Generate AI-powered answers using Amazon Bedrock
* 💬 Interactive question-and-answer interface
* 🌐 Web-based frontend
* 🧪 Backend test suite for core RAG components
* 🔐 Environment-based configuration for sensitive values

---

## 🏗️ Architecture

The application consists of two primary layers:

### Frontend

The frontend provides the user interface for:

* Uploading documents
* Entering questions
* Displaying retrieved answers
* Viewing the conversation

Technologies:

* HTML
* CSS
* JavaScript

### Backend

The backend manages:

* PDF/document processing
* Text chunking
* Embedding generation
* Retrieval
* Prompt construction
* LLM interaction
* API endpoints

Technologies:

* Python
* Flask
* Amazon Bedrock

---

## 🧠 RAG Pipeline

The application follows a Retrieval-Augmented Generation pipeline.

### 1. Document Upload

The user uploads a PDF document through the web interface.

### 2. Text Extraction

Text is extracted from the uploaded document.

### 3. Text Chunking

The extracted text is divided into smaller chunks so that relevant sections can be efficiently retrieved.

### 4. Embedding Generation

The document chunks are converted into numerical vector representations called **embeddings**.

These vectors represent the semantic meaning of the text.

### 5. Retrieval

When a user asks a question, the question is converted into an embedding and compared with the document chunk embeddings.

The most relevant chunks are selected as context.

### 6. Prompt Construction

The retrieved document context is combined with the user's question to construct a prompt for the language model.

### 7. AI Generation

Amazon Bedrock processes the prompt and generates a response based on the retrieved document context.

---

## ☁️ AWS Services

The project integrates with AWS services for AI functionality and deployment.

| AWS Service        | Purpose                                                  |
| ------------------ | -------------------------------------------------------- |
| **Amazon Bedrock** | Provides access to foundation models and AI capabilities |
| **Amazon EC2**     | Hosts the application for deployment                     |

> Additional AWS services can be added as the project evolves.

---

## 📂 Project Structure

```text
ai-document-rag/
│
├── backend/
│   ├── app.py
│   ├── requirements.txt
│   │
│   ├── services/
│   │   ├── embeddings.py
│   │   ├── llm.py
│   │   ├── prompt.py
│   │   ├── rag.py
│   │   └── text_chunker.py
│   │
│   ├── test_embedings.py
│   ├── test_llm.py
│   ├── test_pipeline.py
│   └── test_rag.py
│
├── frontend/
│   ├── index.html
│   ├── script.js
│   └── style.css
│
├── data/
│   └── sample_rag_document.pdf
│
├── .gitignore
└── README.md
```

---

## ⚙️ Prerequisites

Before running the application locally, make sure you have:

* Python 3.x
* pip
* An AWS account
* Appropriate Amazon Bedrock model access
* AWS credentials configured for the application

---

## 🚀 Installation

### 1. Clone the repository

```bash
git clone https://github.com/hkrish2266/ai-document-rag.git
```

```bash
cd ai-document-rag
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

### 3. Activate the virtual environment

**Windows:**

```bash
.venv\Scripts\activate
```

**Linux / macOS:**

```bash
source .venv/bin/activate
```

### 4. Install dependencies

```bash
pip install -r backend/requirements.txt
```

---

## 🔐 Configuration

Sensitive configuration should **never be committed to GitHub**.

The project uses environment-based configuration where applicable.

Create a `.env` file for local configuration:

```text
AWS_REGION=your-aws-region
```

Add any additional configuration required by your selected Bedrock models.

> ⚠️ Never commit AWS access keys, secret keys, passwords, tokens, or other credentials to GitHub.

The `.gitignore` file is configured to prevent `.env` files from being committed.

---

## ▶️ Running the Application

From the project root:

```bash
python backend/app.py
```

Once the backend is running, open the application in your browser using the address provided by the Flask server.

---

## 💬 Example Usage

### Upload a document

```text
Upload PDF
      ↓
Document processed
      ↓
Text chunks created
```

### Ask a question

```text
User:
"What is Amazon EC2?"

        ↓

RAG Retrieval

        ↓

Relevant document context

        ↓

Amazon Bedrock

        ↓

AI:
"Amazon EC2 is a compute service..."
```

The generated response is based on the relevant information retrieved from the uploaded document.

---

## 🧪 Testing

The backend includes tests for important components of the RAG pipeline.

```text
backend/
├── test_embedings.py
├── test_llm.py
├── test_pipeline.py
└── test_rag.py
```

Tests can be executed using Python's testing tools depending on the project configuration.

---

## 🔒 Security Considerations

The project follows basic security practices:

* Credentials are kept outside the source code.
* `.env` files are excluded from Git.
* Virtual environments are excluded from Git.
* AWS credentials should be managed through appropriate AWS authentication mechanisms.
* Sensitive configuration should never be committed to the repository.

---

## 🚀 Deployment

The application has been deployed on **Amazon EC2** as part of the AWS project.

The deployment architecture is:

```text
                Internet
                    │
                    ▼
              Amazon EC2
                    │
              ┌─────┴─────┐
              │           │
          Frontend     Backend
                          │
                          ▼
                   Amazon Bedrock
                          │
                          ▼
                     AI Model
```

---

## 🛠️ Technology Stack

### Application

* Python
* Flask
* HTML
* CSS
* JavaScript

### AI / RAG

* Retrieval-Augmented Generation
* Text chunking
* Embeddings
* Semantic retrieval
* Large Language Models

### AWS

* Amazon Bedrock
* Amazon EC2

### Development

* Git
* GitHub
* Python virtual environment

---

## 📈 Future Improvements

Potential improvements include:

* 🔎 Dedicated vector database
* 📚 Support for multiple documents
* 💾 Persistent document storage
* 👥 User authentication
* 💬 Persistent conversation history
* 📊 RAG evaluation and monitoring
* ⚡ Improved retrieval strategies
* 🐳 Docker-based deployment
* 🔄 Automated CI/CD deployment
* ☁️ Additional AWS managed services

---

## 🎯 Project Goals

This project demonstrates practical implementation of:

* Generative AI
* Retrieval-Augmented Generation
* Document question answering
* Embeddings and semantic retrieval
* Python backend development
* Frontend integration
* AWS cloud deployment
* Amazon Bedrock integration
* Git/GitHub version control

---

## 👨‍💻 Author

**Hari Krishna Madaka**

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Hari%20Krishna%20Madaka-blue?style=flat-square\&logo=linkedin)](https://www.linkedin.com/in/hari-krishna-madaka/)

[![LeetCode](https://img.shields.io/badge/LeetCode-hari__21072007-orange?style=flat-square\&logo=leetcode)](https://leetcode.com/u/hari_21072007/)

[![GitHub](https://img.shields.io/badge/GitHub-hkrish2266-black?style=flat-square\&logo=github)](https://github.com/hkrish2266)

### Profiles

* 💼 LinkedIn — [Hari Krishna Madaka](https://www.linkedin.com/in/hari-krishna-madaka/)
* 🧩 LeetCode — [hari_21072007](https://leetcode.com/u/hari_21072007/)
* 🐙 GitHub — [hkrish2266](https://github.com/hkrish2266)

---

## ⭐ Project

If you find this project useful or interesting, consider giving the repository a ⭐ on GitHub.

---

**Built with Python, AWS, Amazon Bedrock, and RAG.**
