import os
from typing import Dict, Any
from langchain.memory import ConversationBufferMemory
from langchain.prompts import PromptTemplate
from langchain.chains import ConversationChain
from langchain_openai import ChatOpenAI
from langchain_core.documents import Document
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.chains import RetrievalQA
from .cv_data import CV_DATA, INTERVIEW_CONTEXT

class CVAgent:
    def __init__(self):
        self.api_key = os.getenv("OPENAI_API_KEY")
        if not self.api_key:
            raise ValueError("OpenAI API key not found in environment variables")
        
        self.llm = ChatOpenAI(
            temperature=0.7,
            openai_api_key=self.api_key,
            model_name="gpt-3.5-turbo"
        )
        
        self.embeddings = OpenAIEmbeddings(openai_api_key=self.api_key)
        self.sessions: Dict[str, Any] = {}
        self.vector_store = self._create_vector_store()
        self.qa_chain = self._create_qa_chain()
        
    def _create_vector_store(self):
        """Create vector store from CV data for RAG"""
        documents = []
        
        # Personal info
        personal_doc = Document(
            page_content=f"Name: {CV_DATA.personal_info['name']}\n"
                        f"Title: {CV_DATA.personal_info['title']}\n"
                        f"Location: {CV_DATA.personal_info['location']}\n"
                        f"Summary: {CV_DATA.personal_info['summary']}",
            metadata={"section": "personal_info"}
        )
        documents.append(personal_doc)
        
        # Experience
        for exp in CV_DATA.experience:
            exp_content = f"Company: {exp['company']}\n" \
                         f"Role: {exp['role']}\n" \
                         f"Period: {exp['period']}\n" \
                         f"Responsibilities: {'; '.join(exp['responsibilities'])}\n" \
                         f"Technologies: {', '.join(exp['technologies'])}"
            documents.append(Document(
                page_content=exp_content,
                metadata={"section": "experience", "company": exp['company']}
            ))
        
        # Education
        for edu in CV_DATA.education:
            edu_content = f"Institution: {edu['institution']}\n" \
                         f"Degree: {edu['degree']}\n" \
                         f"Period: {edu['period']}\n" \
                         f"Achievements: {'; '.join(edu.get('achievements', []))}"
            documents.append(Document(
                page_content=edu_content,
                metadata={"section": "education"}
            ))
        
        # Skills
        for category, skills in CV_DATA.skills.items():
            skills_content = f"Skill Category: {category.replace('_', ' ').title()}\n" \
                           f"Skills: {', '.join(skills)}"
            documents.append(Document(
                page_content=skills_content,
                metadata={"section": "skills", "category": category}
            ))
        
        # Projects
        for project in CV_DATA.projects:
            project_content = f"Project: {project['name']}\n" \
                            f"Description: {project['description']}\n" \
                            f"Technologies: {', '.join(project['technologies'])}\n" \
                            f"Features: {'; '.join(project['features'])}"
            documents.append(Document(
                page_content=project_content,
                metadata={"section": "projects", "project": project['name']}
            ))
        
        # Achievements
        achievements_content = f"Professional Achievements:\n" + "\n".join(f"- {achievement}" for achievement in CV_DATA.achievements)
        documents.append(Document(
            page_content=achievements_content,
            metadata={"section": "achievements"}
        ))
        
        # Create vector store
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
        split_docs = text_splitter.split_documents(documents)
        
        vector_store = FAISS.from_documents(split_docs, self.embeddings)
        return vector_store
    
    def _create_qa_chain(self):
        """Create RetrievalQA chain for answering questions"""
        retriever = self.vector_store.as_retriever(search_kwargs={"k": 3})
        
        prompt_template = """You are answering interview questions as Prosper Mambambo. Use the following context to answer questions accurately and professionally.

Context from my CV:
{context}

Interview Guidelines: Answer as Prosper Mambambo in first person, being professional yet personable. Use the context to provide accurate information about my background, experience, skills, and projects. Provide specific examples when relevant.

Question: {question}

Answer:"""

        qa_prompt = PromptTemplate(
            template=prompt_template,
            input_variables=["context", "question"]
        )
        
        return RetrievalQA.from_chain_type(
            llm=self.llm,
            chain_type="stuff",
            retriever=retriever,
            chain_type_kwargs={
                "prompt": qa_prompt,
            }
        )
    
    def _get_session_memory(self, session_id: str) -> ConversationBufferMemory:
        """Get or create conversation memory for a session"""
        if session_id not in self.sessions:
            self.sessions[session_id] = ConversationBufferMemory(return_messages=True)
        return self.sessions[session_id]
    
    async def get_response(self, message: str, session_id: str = "default") -> str:
        """Get response from the CV agent"""
        try:
            # Use RAG chain with interview context
            response = self.qa_chain.run(message)
            
            # Store in conversation memory for context
            memory = self._get_session_memory(session_id)
            memory.chat_memory.add_user_message(message)
            memory.chat_memory.add_ai_message(response)
            
            return response
            
        except Exception as e:
            return f"I apologize, but I'm having trouble processing your question right now. Could you please rephrase it? Error: {str(e)}"
    
    def get_conversation_history(self, session_id: str) -> list:
        """Get conversation history for a session"""
        if session_id in self.sessions:
            return self.sessions[session_id].chat_memory.messages
        return []
    
    def clear_session(self, session_id: str):
        """Clear conversation history for a session"""
        if session_id in self.sessions:
            del self.sessions[session_id]