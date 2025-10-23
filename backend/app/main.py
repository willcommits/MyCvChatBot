from fastapi import FastAPI, WebSocket, WebSocketDisconnect, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional
import json
import os
from dotenv import load_dotenv
from .cv_agent import CVAgent
from .models import ChatMessage, ChatResponse

load_dotenv()

app = FastAPI(title="CV Chatbot API", version="1.0.0")

# CORS configuration for React frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with specific frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize CV Agent
cv_agent = CVAgent()

class ConnectionManager:
    def __init__(self):
        self.active_connections: List[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)

    async def send_personal_message(self, message: str, websocket: WebSocket):
        await websocket.send_text(message)

manager = ConnectionManager()

@app.get("/")
async def root():
    return {"message": "CV Chatbot API is running"}

@app.get("/health")
async def health_check():
    return {"status": "healthy"}

@app.post("/chat", response_model=ChatResponse)
async def chat_endpoint(message: ChatMessage):
    try:
        response = await cv_agent.get_response(message.message, message.session_id)
        return ChatResponse(response=response, session_id=message.session_id)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/suggestions")
async def get_suggestions():
    return {
        "questions": [
            "Tell me about your professional background",
            "What are your key technical skills?",
            "Describe your most significant project",
            "What's your experience with Python and AI?",
            "What are your career goals?",
            "Tell me about your education",
            "What makes you a good fit for this role?",
            "Describe your leadership experience",
        ]
    }

@app.websocket("/ws/{session_id}")
async def websocket_endpoint(websocket: WebSocket, session_id: str):
    await manager.connect(websocket)
    try:
        while True:
            data = await websocket.receive_text()
            message_data = json.loads(data)
            
            # Process message through CV agent
            response = await cv_agent.get_response(
                message_data["message"], 
                session_id
            )
            
            # Send response back
            await manager.send_personal_message(
                json.dumps({"response": response, "session_id": session_id}),
                websocket
            )
    except WebSocketDisconnect:
        manager.disconnect(websocket)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)