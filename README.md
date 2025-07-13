# Bogie and WheelSpec FastAPI Project

## ✅ Setup Instructions

1. Clone the repo or unzip the code.
2. Navigate to the project folder: cd project-folder
3. Create and activate a virtual environment:   python -m venv venv
      venv\Scripts\activate # For Windows or venv\bin\activate
4. Install dependencies: pip install -r requirements.txt
5. Create a `.env` file and add:
      MONGO_URL=mongodb://localhost:27017
      MONGO_DB=your_db_name
6. Run the app:
      uvicorn main:app --reload

Access API Docs at: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

## 💻 Tech Stack Used

- FastAPI
- Pydantic
- Motor (MongoDB async driver)
- Uvicorn
- MongoDB

---

## ✅ Implemented APIs

### 1. `POST /api/bogie-checksheet`
- **Function**: Submits a bogie inspection form.
- **Body**: JSON object with bogie details and status.
- **Response**: 201 Created with status confirmation.

### 2. `GET /api/wheel-specification`
- **Function**: Fetches wheel specs based on query filters.
- **Params**: `formNumber`, `submittedBy`, `submittedDate`
- **Response**: 200 OK with matched data.

---

## ⚠️ Assumptions & Limitations

- Data is stored in a local MongoDB collection.
- No frontend/UI is provided.
