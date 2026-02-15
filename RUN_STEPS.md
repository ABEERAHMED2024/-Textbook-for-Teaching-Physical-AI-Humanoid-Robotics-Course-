# Physical AI & Humanoid Robotics Textbook - Setup and Run Instructions

## Project Overview

This project is a comprehensive 13-week textbook for industry practitioners learning Physical AI and Humanoid Robotics. It includes:

- Educational content covering ROS 2, Digital Twins, NVIDIA Isaac, and Vision-Language-Action models
- A RAG-based chatbot for answering questions about the textbook content
- Authentication system for personalized learning experiences
- Content personalization and Urdu translation features

## Prerequisites

- Node.js 18+ and npm
- Python 3.8+
- Access to OpenAI API (for embeddings and chat)
- Access to Qdrant (vector database)
- PostgreSQL-compatible database (Neon recommended)

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/ameen-alam/Physical-AI-Humanoid-Robotics-Textbook.git
cd Physical-AI-Humanoid-Robotics-Textbook
```

### 2. Frontend Setup (Docusaurus)

```bash
# Install frontend dependencies
npm install

# Create environment file
cp .env.example .env

# Edit .env to set your backend API URL
# For local development: REACT_APP_API_URL=http://localhost:8000
```

### 3. Backend Setup (FastAPI)

```bash
# Navigate to the server directory
cd server

# Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install backend dependencies
pip install -r requirements.txt

# Create environment file
cp .env.example .env

# Edit .env with your API keys and database URL
# OPENAI_API_KEY=your_openai_api_key
# QDRANT_URL=your_qdrant_url
# QDRANT_API_KEY=your_qdrant_api_key
# NEON_DATABASE_URL=your_neon_database_url
# JWT_SECRET_KEY=your_jwt_secret_key
# AUTH_SECRET=your_auth_secret
```

### 4. Setting up the Vector Database (Qdrant)

The RAG system requires a populated Qdrant vector database with textbook content. Follow these steps:

```bash
# In the server directory
cd server

# Run the ingestion script to populate the vector database
python scripts/ingest_content.py
```

## Running the Application

### 1. Start the Backend Server

```bash
# In the server directory
cd server
source venv/bin/activate  # Activate virtual environment if needed

# Start the backend server
uvicorn main:app --reload --port 8000
```

### 2. Start the Frontend (Docusaurus)

In a new terminal:

```bash
# In the project root directory
npm start
```

The application will be available at `http://localhost:3000`.

## Deployment Instructions

### Deploying to Vercel (Frontend)

1. Fork this repository
2. Log in to Vercel and import your forked repository
3. Set the build command to `npm run build`
4. Set the output directory to `build`
5. Add environment variables:
   - `REACT_APP_API_URL`: Your backend API URL
6. Deploy

### Deploying the Backend

The backend needs to be deployed separately. You can use platforms like:

- Railway
- Heroku
- AWS
- Google Cloud Run

Make sure to set the same environment variables as in your local setup.

## Features

### 1. RAG Chatbot
- Ask questions about the textbook content
- Get responses with citations to relevant chapters
- Available as a floating chat widget on all pages

### 2. Authentication System
- Sign up with email and password
- Provide software and hardware background information
- Personalized learning experience based on your background

### 3. Content Personalization
- Click "Personalize Content" button on any chapter to get content tailored to your background
- Available after signing in

### 4. Urdu Translation
- Click "Translate to Urdu" button on any chapter to get content translated
- Available after signing in

## Troubleshooting

### Common Issues

1. **Backend not connecting to frontend**:
   - Ensure the backend server is running on port 8000
   - Check that `REACT_APP_API_URL` is set correctly in the frontend environment

2. **Vector database not populated**:
   - Run the ingestion script to populate the Qdrant database with textbook content

3. **Authentication not working**:
   - Ensure JWT_SECRET_KEY and AUTH_SECRET are set in the backend environment
   - Check that the database connection is working

### Environment Variables

Make sure all required environment variables are set in both frontend and backend:

**Frontend (.env)**:
- `REACT_APP_API_URL`: Backend API URL

**Backend (server/.env)**:
- `OPENAI_API_KEY`: OpenAI API key
- `QDRANT_URL`: Qdrant vector database URL
- `QDRANT_API_KEY`: Qdrant API key
- `NEON_DATABASE_URL`: PostgreSQL database URL
- `JWT_SECRET_KEY`: Secret for JWT tokens
- `AUTH_SECRET`: Secret for authentication

## Development

To run tests:

```bash
# Frontend tests
npm test

# Backend tests
cd server
python -m pytest
```

To build for production:

```bash
# Frontend build
npm run build
```

## Architecture

- **Frontend**: Docusaurus-based static site with React components
- **Backend**: FastAPI server with RAG capabilities
- **Vector Database**: Qdrant for semantic search
- **Relational Database**: PostgreSQL (Neon) for user data and chat history
- **Authentication**: Custom JWT-based authentication system