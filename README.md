# Flask & FastAPI - Week 1 🚀

This repository contains my daily progress in learning **Flask** and **FastAPI**.  
I am building step by step, testing features, and documenting my learning journey.  

---

## 📅 Progress Log

### ✅ Day 1
- Set up project structure  
- Created virtual environment `.venv`  
- Installed FastAPI and Uvicorn  
- Made sure app runs with `uvicorn main:app --reload`  

### ✅ Day 2
- Added first route (`/`) returning JSON response  
- Learned about `@app.get` decorators  

### ✅ Day 3
- Implemented **query parameters**  
- Created endpoints with optional parameters  

### ✅ Day 4
- Introduced **Pydantic models** for request validation  
- Added a **POST endpoint** `/items`  
- Tested JSON request body in **Swagger UI**  
- Example tested:  

```json
{
  "name": "Laptop",
  "price": 1200.5,
  "in_stock": true,
  "description": "Gaming laptop"
}
