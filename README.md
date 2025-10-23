# CV Chatbot - Interactive Professional Assistant

An AI-powered chatbot that allows interactive conversations about Prosper Mambambo's professional background, built with LangChain, FastAPI, and React.

## 🚀 Live Demo

- **Frontend**: [Live on Netlify](https://prospercvchatbot.netlify.app/)

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

## 🐳 Docker Support

### Backend Docker
```bash
cd backend
docker build -t cv-chatbot-api .
docker run -p 8000:8000 -e OPENAI_API_KEY=your_key cv-chatbot-api
```
