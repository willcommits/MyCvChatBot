# CV Chatbot Deployment Guide

## Quick Start Instructions

### 1. Backend Deployment on Railway (Recommended)

1. **Deploy to Railway**:
   - Go to [railway.app](https://railway.app) and sign up/login
   - Click "New Project" → "Deploy from GitHub repo"
   - Connect your GitHub repository
   - Railway will automatically detect the configuration from `railway.json` and `nixpacks.toml`

2. **Set Environment Variables**:
   - In Railway dashboard, go to Variables tab
   - Add: `OPENAI_API_KEY` = `your_actual_openai_api_key`

3. **Deploy**: Railway will automatically build and deploy using the configuration files
   - The app will deploy to your Railway account's default region
   - To change the region, go to Settings → Deployment Region in Railway dashboard
   - Health checks will use the `/health` endpoint
   - The app will restart automatically on failure

**Note**: The repository includes these configuration files for Railway deployment:
- `start.sh` - Entry point script that starts the gunicorn server (automatically used by Railway)
- `Procfile` - Process definition for platform compatibility (defines the web service)
- `nixpacks.toml` - Nixpacks build configuration specifying Python 3.11 and build commands
- `railway.json` - Railway-specific settings including health checks and restart policies
- `requirements.txt` - Root-level Python dependency reference (enables Python language detection)

**No modifications needed** - these files work automatically with the backend configuration.

### 2. Alternative: Backend Deployment on Render

1. **Create GitHub Repository**:
   - Push the entire `Chatbot` folder to a new GitHub repository
   - Make sure the repository is public or connect your GitHub account to Render

2. **Deploy to Render**:
   - Go to [render.com](https://render.com) and sign up/login
   - Click "New" → "Web Service"
   - Connect your GitHub repository
   - Configure the service:
     - **Name**: `cv-chatbot-api` (or your preferred name)
     - **Root Directory**: `backend`
     - **Environment**: `Python 3`
     - **Build Command**: `pip install -r requirements.txt`
     - **Start Command**: `gunicorn --bind 0.0.0.0:$PORT --workers 2 --worker-class uvicorn.workers.UvicornWorker app.main:app`

3. **Set Environment Variables**:
   - In Render dashboard, go to Environment tab
   - Add: `OPENAI_API_KEY` = `your_actual_openai_api_key`

4. **Deploy**: Click "Create Web Service" - Render will build and deploy automatically

### 3. Frontend Deployment on Vercel

1. **Deploy to Vercel**:
   - Go to [vercel.com](https://vercel.com) and sign up/login
   - Click "New Project"
   - Import your GitHub repository
   - Configure the project:
     - **Framework Preset**: `Vite`
     - **Root Directory**: `frontend`
     - **Build Command**: `npm run build`
     - **Output Directory**: `dist`

2. **Set Environment Variables**:
   - In Vercel dashboard, go to Settings → Environment Variables
   - Add: `VITE_API_URL` = `your_render_backend_url` (e.g., `https://cv-chatbot-api.onrender.com`)

3. **Deploy**: Click "Deploy" - Vercel will build and deploy automatically

## Alternative: Local Testing

### Backend (Terminal 1):
```bash
cd backend
python -m venv venv
source venv/bin/activate  # Windows: venv\\Scripts\\activate
pip install -r requirements.txt
# Create .env file with OPENAI_API_KEY=your_key
uvicorn app.main:app --reload --port 8000
```

### Frontend (Terminal 2):
```bash
cd frontend
npm install
npm run dev
```

Visit `http://localhost:3000` to test the application.

## Post-Deployment

### Testing Your Deployed Application
1. Visit your Vercel frontend URL
2. Try asking questions like:
   - "Tell me about your background"
   - "What are your technical skills?"
   - "Describe your experience with Python"

### Sharing with Employers
- **Frontend URL**: Share the Vercel deployment URL
- **Demo Instructions**: "This is an interactive CV chatbot - ask me anything about my professional background!"

## Troubleshooting

### Common Issues

1. **Backend not responding**:
   - Check Render logs for errors
   - Verify OpenAI API key is set correctly
   - Ensure all dependencies are installed

2. **Frontend can't connect to backend**:
   - Check VITE_API_URL environment variable
   - Verify CORS settings in backend
   - Check browser console for network errors

3. **OpenAI API errors**:
   - Verify API key has sufficient credits
   - Check API key permissions
   - Monitor rate limits

4. **Worker timeout on deployment** (FIXED):
   - The application uses lazy initialization for the AI agent
   - Health checks respond immediately (within 2-3 seconds)
   - First chat request may take longer (~10-15 seconds) as it initializes the AI agent
   - Subsequent requests are fast as the agent remains in memory

### Support Resources
- Render Documentation: [render.com/docs](https://render.com/docs)
- Vercel Documentation: [vercel.com/docs](https://vercel.com/docs)
- OpenAI API Documentation: [platform.openai.com/docs](https://platform.openai.com/docs)

## Technical Notes

### Lazy Initialization
The CV Agent (which includes OpenAI embeddings and FAISS vector store) is initialized on the first request rather than at startup. This approach:
- Allows workers to start quickly and bind to ports within Render's timeout
- Reduces memory usage on the free tier
- Enables successful health checks during deployment
- First chat request may take 10-15 seconds while subsequent requests are fast

## Performance Optimization

### For Production Use
1. **Backend**:
   - Upgrade Render plan for better performance
   - Implement caching for frequent requests
   - Add request rate limiting

2. **Frontend**:
   - Enable Vercel Analytics
   - Optimize bundle size
   - Add performance monitoring

## Security Considerations

1. **API Keys**: Never commit API keys to version control
2. **CORS**: Configure specific origins in production
3. **Rate Limiting**: Implement appropriate request limits
4. **Environment Variables**: Use platform-specific environment variable management

---

**Need Help?** Contact Prosper Mambambo with any deployment questions.