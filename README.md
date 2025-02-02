# Helix Project

A modern web application built with a **React** frontend, **Flask** backend, and **OpenAI integration** for AI capabilities.

## Architecture Overview

The application consists of three main layers:

- **React Frontend**: Handles user interface and state management.
- **Flask Backend**: Provides REST API endpoints and business logic.
- **OpenAI Integration**: Powers AI features through language models.

## Prerequisites

Before setting up the project, ensure you have the following installed:

- [Node.js](https://nodejs.org/) (v16 or higher)
- [Python](https://www.python.org/) (v3.8 or higher)
- **npm** or **yarn** package manager
- [OpenAI API key](https://beta.openai.com/signup/)

---

## Setup Instructions

### Backend Setup

1. **Navigate to the backend directory:**
   ```bash
   cd backend
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment:**
   - **Windows:**
     ```bash
     venv\Scripts\activate
     ```
   - **macOS/Linux:**
     ```bash
     source venv/bin/activate
     ```

4. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

5. **Add your OpenAI API key in the `.env` file (create this file in the `backend/` folder):**
   ```
   OPENAI_API_KEY=your_api_key_here
   ```

6. **Start the Flask server:**
   ```bash
   python run.py
   ```

   The backend server will start on port **8080**: [http://localhost:8080](http://localhost:8080)

---

### Frontend Setup

1. **Navigate to the frontend directory:**
   ```bash
   cd frontend
   ```

2. **Install dependencies:**
   ```bash
   npm install
   # or
   yarn install
   ```

3. **Start the development server:**
   ```bash
   npm run dev
   ```

   The frontend development server will start on port **5173**: [http://localhost:5173](http://localhost:5173)

---

## Project Structure

```
helix/
├── frontend/          # React frontend application
│   ├── src/          # Frontend source code
│   ├── public/       # Static assets
│   ├── package.json  # Frontend dependencies
│   └── README.md     # Frontend documentation
├── backend/           # Flask backend application
│   ├── .env          # Environment variables (create this)
│   ├── requirements.txt  # Backend dependencies
│   ├── run.py        # Flask application entry point
│   ├── app/          # Application logic
│   └── models/       # Database models
└── README.md         # Project documentation
```



