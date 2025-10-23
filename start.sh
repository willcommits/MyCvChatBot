#!/bin/bash

# Navigate to backend directory and start the application
cd backend
exec gunicorn -c gunicorn.conf.py app.main:app
