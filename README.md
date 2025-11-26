#coding challenge
# Math Question Refinement Chatbot  
A minimal full-stack chatbot application that analyzes, validates, and refines math questions using FastAPI, LangChain, and OpenAI. It includes a lightweight HTML + JavaScript frontend.


## Overview  
This project provides a simple interface where users can input a math-related question.  
The backend evaluates the question using an LLM, determines whether it is valid, generates a refined version, and optionally returns similar questions stored locally.

The purpose is to demonstrate:  
- FastAPI backend development  
- Integration with OpenAI via LangChain  
- Clean request/response schema design  
- Simple frontend interaction using Fetch API  
- Minimal and maintainable project structure



## Project Structure  

Chatbot-Project/
│
├── backend/
│   ├── app/
│   │   ├── main.py          # FastAPI initialization
│   │   ├── router.py        # API routing and /chat endpoint
│   │   ├── llm.py           # LangChain + OpenAI logic
│   │   ├── schemas.py       # Pydantic models
│   │   ├── vectorstore.py   # Hardcoded similar questions
│   │   ├── loader.py        # Loads sample questions from JSON
│   │   ├── question.json    # Sample dataset
│   └── venv/                # Virtual environment (ignored in Git)
│
└── frontend/
    ├── index.html           # Simple user interface
    └── script.js            # Fetch request to backend




## Technologies Used  

### Backend  
- Python 3.10+  
- FastAPI  
- Pydantic  
- LangChain  
- OpenAI Chat Completions API  

### Frontend  
- HTML  
- JavaScript (Fetch API)



## Running the Backend  

### Step 1: Navigate to backend directory  
```bash
cd backend


### Step 2: Activate the virtual environment  
```bash
.\venv\Scripts\activate        # Windows


### Step 3: Set your OpenAI API key  
```bash
$env:OPENAI_API_KEY = "your-api-key-here"


### Step 4: Start the FastAPI server  
```bash
uvicorn app.main:app --reload --port 9000


### Step 5: Test API using Swagger  
Open in browser:  

http://127.0.0.1:9000/docs



## Running the Frontend  

### Step 1: Navigate to the frontend folder  
```bash
cd frontend


### Step 2: Open the HTML file  
```bash
start index.html        # Windows


The frontend communicates with the backend using:  
```
http://127.0.0.1:9000/chat/
```

---

## API Endpoint Details  

### POST /chat/  
**Request Body**  
```json
{
  "message": "What is 2+2?"
}
```

**Response Body**  
```json
{
  "original_question": "",
  "is_valid": true,
  "refined_question": "",
  "similar_questions": []
}
```

---

## How the System Works  
1. The user submits a question from the frontend.  
2. The message is sent to the FastAPI backend.  
3. LangChain formats the prompt and interacts with the OpenAI model.  
4. The backend validates and refines the question.  
5. A JSON response is returned with the refined question and similar samples.  
6. The frontend displays the output in a simple chat-style interface.
