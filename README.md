# CV Chatbot - Interactive Professional Assistant

An AI-powered chatbot that allows interactive conversations about Prosper Mambambo's professional background, built with LangChain, FastAPI, and React.

## 🚀 Live Demo

- **Frontend**: Coming soon (will be deployed on Vercel)
- **Backend API**: Coming soon (will be deployed on Render)

## 🏗️ Architecture

### Backend (Python + FastAPI + LangChain)
- **FastAPI** for REST API and WebSocket support
- **LangChain** with RAG (Retrieval Augmented Generation) for intelligent responses
- **OpenAI GPT-3.5-turbo** for natural language processing
- **FAISS** vector database for CV content retrieval
- **Render-optimized** deployment configuration

### Frontend (React + TypeScript)
- **Modern React** with hooks and TypeScript
- **TailwindCSS** for responsive, professional styling
- **Real-time chat interface** with message history
- **Question suggestions** for easy interaction
- **Mobile-responsive** design

## 🛠️ Local Development

### Prerequisites
- Python 3.11+
- Node.js 18+
- OpenAI API key

### Backend Setup

1. **Navigate to backend directory**:
   ```bash
   cd backend
   ```

2. **Create virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\\Scripts\\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**:
   ```bash
   cp .env.example .env
   # Edit .env and add your OpenAI API key
   ```

5. **Run the development server**:
   ```bash
   uvicorn app.main:app --reload --port 8000
   ```

   The API will be available at `http://localhost:8000`

### Frontend Setup

1. **Navigate to frontend directory**:
   ```bash
   cd frontend
   ```

2. **Install dependencies**:
   ```bash
   npm install
   ```

3. **Set up environment variables**:
   ```bash
   cp .env.example .env
   # The default settings should work for local development
   ```

4. **Run the development server**:
   ```bash
   npm run dev
   ```

   The frontend will be available at `http://localhost:3000`

## 🚀 Deployment

### Backend Deployment (Render)

1. **Push code to GitHub repository**
2. **Connect to Render**:
   - Go to [render.com](https://render.com)
   - Create new Web Service
   - Connect your GitHub repository
   - Select the `backend` folder

3. **Configure environment variables in Render dashboard**:
   - `OPENAI_API_KEY`: Your OpenAI API key

4. **Deploy**: Render will automatically build and deploy using the `render.yaml` configuration

### Frontend Deployment (Vercel)

1. **Push code to GitHub repository**
2. **Deploy to Vercel**:
   - Go to [vercel.com](https://vercel.com)
   - Import your GitHub repository
   - Set root directory to `frontend`
   - Set environment variable `VITE_API_URL` to your Render backend URL

## 📝 API Documentation

Once the backend is running, visit `http://localhost:8000/docs` for interactive API documentation.

### Key Endpoints
- `POST /chat` - Send message and get AI response
- `GET /suggestions` - Get suggested interview questions
- `GET /health` - Health check endpoint
- `WebSocket /ws/{session_id}` - Real-time chat communication

## 🎯 Features

### For Interviewers & Recruiters
- **Natural conversation** about professional background
- **Specific examples** and detailed responses
- **Organized information** about experience, skills, and projects
- **Professional presentation** of qualifications

### Technical Features
- **RAG-powered responses** using CV content as knowledge base
- **Conversation memory** maintains context within sessions
- **Responsive design** works on all devices
- **Real-time interaction** with loading states and typing indicators
- **Suggested questions** to guide conversations

## 🔧 Customization

### Updating CV Information
Edit `backend/app/cv_data.py` to update:
- Personal information
- Work experience
- Education
- Skills
- Projects
- Achievements

### Modifying AI Behavior
Edit `backend/app/cv_data.py` in the `INTERVIEW_CONTEXT` section to adjust:
- Response tone and style
- Key talking points
- Interview focus areas

## 🐳 Docker Support

### Backend Docker
```bash
cd backend
docker build -t cv-chatbot-api .
docker run -p 8000:8000 -e OPENAI_API_KEY=your_key cv-chatbot-api
```

## 📊 Technical Details

### Backend Stack
- **FastAPI**: Modern, fast web framework for building APIs
- **LangChain**: Framework for developing applications with LLMs
- **OpenAI API**: GPT-3.5-turbo for natural language processing
- **FAISS**: Vector database for efficient similarity search
- **Pydantic**: Data validation using Python type annotations

### Frontend Stack
- **React 18**: Latest React with concurrent features
- **TypeScript**: Type-safe JavaScript development
- **TailwindCSS**: Utility-first CSS framework
- **Vite**: Fast build tool and development server
- **Axios**: HTTP client for API requests

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make changes and test locally
4. Submit a pull request

## 📄 License

This project is for demonstration purposes as part of a hiring exercise.

---

**Contact**: Prosper Mambambo  
**Purpose**: Technical assessment for UCook hiring process  
**Built with**: ❤️ and modern web technologies