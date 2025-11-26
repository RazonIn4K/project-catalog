#!/bin/bash

# Get the directory of the script
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

# Function to kill processes on exit
cleanup() {
    echo "Stopping all services..."
    # Kill all child processes of this script
    pkill -P $$
}
trap cleanup EXIT

echo "🚀 Starting Agency OS Services..."

# 1. Start TaskFlow Backend
echo "Starting TaskFlow Backend (Port 8000)..."
cd "$DIR/../taskflow_backend"
if command -v doppler &> /dev/null; then
    doppler run -- uvicorn main:app --reload --port 8000 &
else
    echo "⚠️ Doppler not found. Running without secrets..."
    uvicorn main:app --reload --port 8000 &
fi

# 2. Start Jules Simulator (Lead Gen Engine)
echo "Starting Lead Gen Simulator (Port 8001)..."
cd "$DIR/../../../ops-hub/tools"
uvicorn lead_gen_simulator:app --port 8001 &

# 3. Start Frontend (Stitch Generated)
echo "Starting Stitch Dashboard (Port 5174)..."
cd "$DIR/../stitch_generated_dashboard"
npm run dev -- --host --port 5174 &

# Wait for all background processes
wait
