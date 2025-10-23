# CV Chatbot Deployment Guide

## Quick Start Instructions

### 1. Backend Deployment on Render

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

### 2. Frontend Deployment on Vercel

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

### Support Resources
- Render Documentation: [render.com/docs](https://render.com/docs)
- Vercel Documentation: [vercel.com/docs](https://vercel.com/docs)
- OpenAI API Documentation: [platform.openai.com/docs](https://platform.openai.com/docs)

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