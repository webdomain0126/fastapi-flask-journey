🚀 Flask & FastAPI – Week 1

This repository documents my daily progress in learning Flask and FastAPI.
I’m building step by step, testing features, and recording everything I learn.

📅 Progress Log
✅ Day 1

Set up project structure

Created virtual environment .venv

Installed FastAPI and Uvicorn

Verified app runs with:

uvicorn main:app --reload

✅ Day 2

Added first route (/) returning a JSON response

Learned about @app.get decorators

✅ Day 3

Implemented query parameters

Created endpoints with optional parameters

✅ Day 4

Introduced Pydantic models for request validation

Added a POST endpoint /items

Tested JSON request body in Swagger UI

📌 Example tested:

{
  "name": "Laptop",
  "price": 1200.5,
  "in_stock": true,
  "description": "Gaming laptop"
}

🛠️ Tech Stack

Language: Python

Frameworks: FastAPI, Flask (later weeks)

Server: Uvicorn

Tools: VS Code, Git

🚀 How to Run
# Clone the repository
git clone https://github.com/webdomain0126/flask-fastapi-week1.git
cd flask-fastapi-week1

# Create a virtual environment
python -m venv .venv
source .venv/bin/activate   # Mac/Linux
.venv\Scripts\activate      # Windows

# Install dependencies
pip install -r requirements.txt

# Start the FastAPI app
uvicorn main:app --reload

📸 Demo (Optional)

👉 You can add screenshots of your Swagger UI or terminal output here.

👤 Author

Tisa Akhter

🌐 GitHub: webdomain0126

💼 LinkedIn: freelancertisa

⭐ If you find this project useful, please give it a star on GitHub!
