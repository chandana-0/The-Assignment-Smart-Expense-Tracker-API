# Smart Expense Tracker API

A RESTful API built using **FastAPI** for managing personal expenses. The application allows users to create, retrieve, filter, calculate totals, and delete expenses through well-structured HTTP endpoints.

This project was developed as part of the **Diligent Software Engineering Apprenticeship 2026 Take-Home Assignment**.

---

## Features

- Create a new expense
- Retrieve all expenses
- Filter expenses by category
- Calculate total expenses
  - Overall expense total
  - Category-wise expense totals
- Delete expenses
- Request validation using Pydantic models
- Interactive API documentation using Swagger UI
- Automated API testing using Pytest

---

## Technology Stack

| Technology | Purpose |
|------------|---------|
| Python 3.11 | Programming language |
| FastAPI | REST API framework |
| Uvicorn | ASGI server |
| Pydantic | Data validation |
| Pytest | Automated testing |
| Git & GitHub | Version control |

---

## Project Structure

```text
Smart-Expense-Tracker-API/

├── README.md
├── AI_NOTES.md
├── requirements.txt
│
├── screenshots/
│   ├── project-structure.png
│   ├── swagger-ui.png
│   ├── create-expense-201.png
│   └── pytest-result.png
│
├── src/
│   ├── __init__.py
│   ├── main.py        # API routes and application entry point
│   ├── models.py      # Request/response data models
│   └── storage.py     # Expense data storage logic
│
└── tests/
    ├── __init__.py
    └── test_main.py   # API test cases
```

---

# Installation & Setup

## 1. Clone Repository

```bash
git clone https://github.com/chandana-0/The-Assignment-Smart-Expense-Tracker-API.git

cd The-Assignment-Smart-Expense-Tracker-API
```

---

## 2. Create Virtual Environment

```bash
python -m venv venv
```

---

## 3. Activate Virtual Environment

### Windows PowerShell

```powershell
venv\Scripts\Activate.ps1
```

### Windows Command Prompt

```cmd
venv\Scripts\activate
```

### macOS/Linux

```bash
source venv/bin/activate
```

---

## 4. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Running the Application

Start the FastAPI server:

```bash
uvicorn src.main:app --reload
```

The API will be available at:

```
http://127.0.0.1:8000
```

---

# API Documentation

FastAPI automatically provides interactive API documentation.

### Swagger UI

```
http://127.0.0.1:8000/docs
```

### OpenAPI Specification

```
http://127.0.0.1:8000/openapi.json
```

---

# Running Tests

Execute the test suite:

```bash
pytest -v
```

Expected output:

```text
10 passed
```

---

# API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/expenses` | Create a new expense |
| GET | `/expenses` | Retrieve all expenses |
| GET | `/expenses?category={category}` | Filter expenses by category |
| GET | `/expenses/total` | Calculate overall and category-wise totals |
| DELETE | `/expenses/{id}` | Delete an expense |

---

# Example API Request

## Create Expense

**POST**

```
/expenses
```

Request Body:

```json
{
  "title": "Groceries",
  "amount": 500,
  "category": "Food",
  "date": "2026-07-31"
}
```

---

## API Response (201 Created)

The API successfully creates a new expense and returns HTTP status code **201 Created**.

Response:

```json
{
  "id": 1,
  "title": "Groceries",
  "amount": 500,
  "category": "Food",
  "date": "2026-07-31"
}
```

HTTP Status:

```
201 Created
```

Screenshot:

![Create Expense 201 Response](Screen%20shots/create-expense-201.png)

---

# Screenshots

## Project Structure

VS Code Explorer showing the organized project structure.

![Project Structure](Screen%20shots/project-structure.png)

---

## Swagger API Documentation

Interactive API documentation provided by FastAPI Swagger UI.

![Swagger UI](Screen%20shots/swagger-ui.png)

## Test Execution

Automated tests executed successfully using Pytest.

![Pytest Results](Screen%20shots/pytest-result.png)

---

# Implementation Details

## Architecture

The project follows a modular structure:

### main.py
- Defines API endpoints
- Handles HTTP requests and responses

### models.py
- Defines Pydantic schemas
- Validates incoming data

### storage.py
- Handles expense storage operations

### tests/
- Contains automated API test cases

---

# Design Decisions

- **FastAPI** was selected because of its performance, simplicity, and automatic OpenAPI documentation generation.
- **Pydantic models** ensure request validation and consistent API responses.
- The application uses an in-memory storage approach because database persistence was not required for this assignment.
- The project is separated into modules to improve readability, maintainability, and testing.
- Pytest test cases verify the core API functionality.

---

# Future Improvements

Possible enhancements:

- Add database support using PostgreSQL or SQLite
- Add user authentication and authorization
- Add expense update functionality
- Add pagination for large expense records
- Add Docker support for deployment

---
# Conclusion

- The Smart Expense Tracker API successfully meets the requirements of the Diligent Software Engineering Apprenticeship 2026 Take-Home Assignment. The project demonstrates a clean, modular, and well-tested RESTful API built with    FastAPI, following good software engineering practices and providing a solid foundation for future enhancements.
---
# Author

***Gaddapara Chandana***

***Diligent Software Engineering Apprenticeship 2026 Candidate***
