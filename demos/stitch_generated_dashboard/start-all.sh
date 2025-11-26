#!/bin/bash

# Get the directory of the script
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

echo "🚀 Starting Agency OS Demo Stack..."

# 1. Start TaskFlow Backend (The Brain)
echo "Starting TaskFlow Backend (Port 8000)..."
if lsof -i :8000 > /dev/null; then
    echo "Port 8000 is already in use. Skipping TaskFlow start."
else
    cd "$DIR/../taskflow_backend"
    # Use Doppler if available, else standard uvicorn
    if command -v doppler &> /dev/null; then
        doppler run -- uvicorn main:app --reload --port 8000 &
    else
        uvicorn main:app --reload --port 8000 &
    fi
fi

# 2. Start Mock Backend (Lead Gen Engine)
echo "Starting Mock Backend (Port 8001)..."
cd "$DIR/../../../ops-hub/tools"
uvicorn mock_backend:app --port 8001 &

# 3. Start Frontend (Stitch Generated)
echo "Starting Stitch Dashboard (Port 5174)..."
cd "$DIR"
npm run dev -- --host --port 5174 &

# Wait for all background processes
wait
