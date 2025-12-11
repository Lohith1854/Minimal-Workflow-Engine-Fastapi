This project is a simple workflow/graph engine built using FastAPI as required in the Tredence Coding Assignment. It allows defining nodes, connecting them, updating shared state across steps, looping until conditions are met, and running workflows through APIs.

---

## 🚀 Features Implemented

- Nodes as Python functions
- Shared state dictionary flowing between nodes
- Edges using "next" to move from node to node
- Looping support (run a node until a condition becomes false)
- Basic branching logic
- Tool registry for node functions
- FastAPI endpoints for creating and running workflows

---

## 🛠 How to Run the Project

1. Create and activate a virtual environment (Windows):

   python -m venv venv
   .\venv\Scripts\Activate.ps1

2. Install dependencies:

   pip install -r requirements.txt

3. Start the server:

   uvicorn app.main:app --reload --port 8000

4. Open Swagger UI in your browser:

   http://127.0.0.1:8000/docs

---

## 🧪 How to Test Workflow in Swagger UI

### Step 1 — Create a graph
Open **POST /graph/create** and paste:

{
  "nodes": {
    "extract": {"fn_name": "extract_functions", "next": "check"},
    "check": {"fn_name": "check_complexity", "next": "detect"},
    "detect": {"fn_name": "detect_issues", "next": "suggest"},
    "suggest": {
      "fn_name": "suggest_improvements",
      "next": null,
      "loop": {"cond_key": "quality_score", "op": "<", "value": 80, "goto": "suggest"}
    }
  }
}

Copy the returned graph_id.

### Step 2 — Run the workflow

Open **POST /graph/run** and paste:

{
  "graph_id": "YOUR_GRAPH_ID",
  "initial_state": {}
}

You will receive:
- final_state
- execution log
- run_id

### Step 3 — View run state again

Use **GET /graph/state/{run_id}**.

---

## 📂 Project Structure

app/
  main.py
  engine/
    graph.py
    runner.py
    tools.py
  workflows/
    code_review.py
requirements.txt
README.md

---

## 🔧 Possible Improvements (If More Time)

- Database storage for graphs and runs
- WebSocket logs to stream execution
- More advanced branching logic
- Async background execution

---

## 👤 Author

Lohith Narayana
Submitted as part of the Tredence AI Engineering Internship Coding Assignment.
