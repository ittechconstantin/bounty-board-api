# Bounty Board

Bounty Board is a full-stack Python application for managing programming tasks and their rewards. It combines a REST API, persistent database storage and a multi-page web interface.

## Features

- Create, list, complete and delete tasks
- Validate incoming data with Pydantic
- Persist data with SQLAlchemy
- Use SQLite by default or connect to MySQL through an environment variable
- Explore and test the API through Swagger UI
- View tasks and statistics in a multi-page Streamlit interface
- See completion progress, available rewards and category charts

## Technology stack

- Python
- FastAPI
- Pydantic
- SQLAlchemy
- SQLite / MySQL
- Streamlit
- Requests

## Project structure

```text
app/
  main.py       FastAPI routes and application configuration
  database.py   Database connection and session management
  models.py     SQLAlchemy database model
  schemas.py    Pydantic request and response validation
  crud.py       Database operations
frontend/
  app.py        Streamlit entry point
  api_client.py Shared HTTP client
  pages/        Tasks, add-task and dashboard pages
```

## Run locally

### 1. Clone the repository

```bash
git clone https://github.com/ittechconstantin/bounty-board-api.git
cd bounty-board-api
```

### 2. Create and activate a virtual environment

Windows PowerShell:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

macOS or Linux:

```bash
python -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Start the API

```bash
uvicorn app.main:app --reload
```

Open the interactive API documentation at <http://127.0.0.1:8000/docs>.

### 5. Start the Streamlit interface

Open a second terminal in the same folder, activate the virtual environment and run:

```bash
streamlit run frontend/app.py
```

The interface opens at <http://127.0.0.1:8501>.

## Configuration

The application uses SQLite by default, so it works without installing a database server. Configuration examples are available in `.env.example`.

To use MySQL, set `DATABASE_URL` before starting the API:

```text
mysql+pymysql://username:password@localhost:3306/bounty_board
```

Credentials are never stored directly in the Python source code.

## API endpoints

| Method | Endpoint | Purpose |
|---|---|---|
| GET | `/health` | Check whether the API is running |
| GET | `/tasks` | List all tasks |
| GET | `/tasks/{task_id}` | Retrieve one task |
| POST | `/tasks` | Create a validated task |
| PUT | `/tasks/{task_id}/complete` | Mark a task as completed |
| DELETE | `/tasks/{task_id}` | Delete a task |
| GET | `/stats/reward-available` | Calculate open tasks and available rewards |

## Background

This project started as a course exercise and was restructured into a standalone portfolio application. The new version separates routing, validation, database access and user-interface concerns, removes hard-coded credentials and provides reproducible setup instructions.

## License

This project is available under the MIT License.
