@echo off
title Autonomous Website Builder & Studio (Port 8503)
cd /d "%~dp0"

echo ========================================================
echo  🚀 Launching Autonomous Website Builder on Port 8503...
echo  🔒 Bound strictly to: http://127.0.0.1:8503
echo ========================================================

python -m streamlit run streamlit_app.py --server.port 8503 --server.address 127.0.0.1 --server.headless false
pause
