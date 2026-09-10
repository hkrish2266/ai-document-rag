# AI Document RAG Assistant

An AI-powered document question-answering application built using
Python, Flask, RAG, embeddings, and Amazon Bedrock.

## Features

- Upload PDF documents
- Extract text from PDFs
- Split documents into chunks
- Generate embeddings
- Perform similarity search
- Retrieve relevant document information
- Generate AI answers
- Display sources
- Maintain chat history
- Simple HTML/CSS/JavaScript frontend

## Architecture

PDF
↓
Text Extraction
↓
Chunking
↓
Embeddings
↓
Vector Search
↓
Relevant Context
↓
Amazon Bedrock
↓
AI Answer
↓
Sources

## Project Structure

AI-Document-RAG/
│
├── backend/
│   ├── app.py
│   ├── requirements.txt
│   │
│   └── services/
│       ├── embeddings.py
│       ├── llm.py
│       ├── prompt.py
│       ├── rag.py
│       └── text_chunker.py
│
├── frontend/
│   ├── index.html
│   ├── script.js
│   └── style.css
│
├── data/
│   └── sample_rag_document.pdf
│
├── tests/
│
├── .env
├── .gitignore
└── README.md

## Technologies

- Python
- Flask
- Flask-CORS
- PyPDF
- Boto3
- Amazon Bedrock
- RAG
- Embeddings
- HTML
- CSS
- JavaScript

## Running Locally

Install the required packages:

pip install -r backend/requirements.txt

Start the backend:

cd backend

python app.py

Then open:

frontend/index.html

## AWS Deployment

The application will be deployed using AWS managed services.

Planned AWS services include:

- Amazon S3
- AWS Lambda
- Amazon API Gateway
- Amazon Bedrock
- Amazon DynamoDB
- Amazon Cognito
- Amazon CloudWatch
- AWS IAM
- Amazon SQS
- Amazon EventBridge