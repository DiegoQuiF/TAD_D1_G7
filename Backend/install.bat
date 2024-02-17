@echo off
virtualenv venv
.\venv\Scripts\activate && pip install -r requirements.txt && cls && py app.py