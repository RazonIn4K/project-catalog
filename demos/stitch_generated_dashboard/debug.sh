#!/bin/bash
echo "--- Node Version ---" > debug.log
node --version >> debug.log 2>&1
echo "--- NPM Version ---" >> debug.log
npm --version >> debug.log 2>&1
echo "--- Node Modules Bin ---" >> debug.log
ls -F node_modules/.bin/ >> debug.log 2>&1
echo "--- NPM Run Dev Output ---" >> debug.log
npm run dev -- --host --port 5174 >> debug.log 2>&1 &
PID=$!
sleep 5
kill $PID
