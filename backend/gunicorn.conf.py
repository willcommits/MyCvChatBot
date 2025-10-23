import os

# Server socket
bind = f"0.0.0.0:{os.environ.get('PORT', '8000')}"
backlog = 2048

# Worker processes
# Use 1 worker on free tier to reduce memory usage
workers = int(os.environ.get('WEB_CONCURRENCY', 1))
worker_class = 'uvicorn.workers.UvicornWorker'
worker_connections = 1000
keepalive = 2

# Restart workers after this many requests, with up to 50% jitter
max_requests = 1000
max_requests_jitter = 50

# Logging
loglevel = 'info'
accesslog = '-'
errorlog = '-'

# Process naming
proc_name = 'cv-chatbot-api'

# Worker timeout - increased to handle first request that initializes CVAgent
# First request may take longer due to lazy initialization
timeout = 120
graceful_timeout = 30

# Preload app to share the CVAgent instance across workers (when using multiple workers)
# This is disabled by default to allow lazy initialization
preload_app = False