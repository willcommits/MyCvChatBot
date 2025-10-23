from pydantic import BaseModel
from typing import Optional, List, Dict, Any

class ChatMessage(BaseModel):
    message: str
    session_id: Optional[str] = "default"

class ChatResponse(BaseModel):
    response: str
    session_id: str

class CVSection(BaseModel):
    title: str
    content: str
    tags: List[str] = []

class CVData(BaseModel):
    personal_info: Dict[str, str]
    experience: List[Dict[str, Any]]
    education: List[Dict[str, Any]]
    skills: Dict[str, List[str]]
    projects: List[Dict[str, Any]]
    achievements: List[str]
    certifications: List[str] = []