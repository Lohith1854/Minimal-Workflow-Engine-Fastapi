<h1>Tredence Coding Assignment – Minimal Workflow/Graph Engine</h1>

<p>
This project is a simple workflow/graph engine built using FastAPI as required in the 
Tredence Coding Assignment. It allows defining nodes, connecting them, updating shared 
state across steps, looping until conditions are met, and running workflows through APIs.
</p>

<hr>

<h2>🚀 Features Implemented</h2>
<ul>
  <li>Nodes as Python functions</li>
  <li>Shared state dictionary flowing between nodes</li>
  <li>Edges using "next" to move from node to node</li>
  <li>Looping support (run a node until a condition becomes false)</li>
  <li>Basic branching logic</li>
  <li>Tool registry for node functions</li>
  <li>FastAPI endpoints for creating and running workflows</li>
</ul>

<hr>

<h2>🛠 How to Run the Project</h2>

<ol>
  <li>Create and activate a virtual environment (Windows):<br><br>
    <pre>
python -m venv venv
.\venv\Scripts\Activate.ps1
    </pre>
  </li>

  <li>Install dependencies:<br><br>
    <pre>
pip install -r requirements.txt
    </pre>
  </li>

  <li>Start the server:<br><br>
    <pre>
uvicorn app.main:app --reload --port 8000
    </pre>
  </li>

  <li>Open Swagger UI:<br><br>
    <a href="http://127.0.0.1:8000/docs">http://127.0.0.1:8000/docs</a>
  </li>
</ol>

<hr>

<h2>🧪 How to Test Workflow in Swagger UI</h2>

<h3>Step 1 — Create a graph</h3>
<p>Open <b>POST /graph/create</b> and paste:</p>

<pre>
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
</pre>

<p>Copy the returned <code>graph_id</code>.</p>

<h3>Step 2 — Run the workflow</h3>

<pre>
{
  "graph_id": "YOUR_GRAPH_ID",
  "initial_state": {}
}
</pre>

<p>You will receive:</p>
<ul>
  <li>final_state</li>
  <li>execution log</li>
  <li>run_id</li>
</ul>

<h3>Step 3 — View run state</h3>
<p>Use <b>GET /graph/state/{run_id}</b>.</p>

<hr>

<h2>📂 Project Structure</h2>

<pre>
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
</pre>

<hr>

<h2>🔧 Possible Improvements (If More Time)</h2>
<ul>
  <li>Database storage for graphs and runs</li>
  <li>WebSocket logs to stream execution</li>
  <li>More advanced branching logic</li>
  <li>Async background execution</li>
</ul>

<hr>

<h2>👤 Author</h2>
<p>
<b>Narayana Lohith</b><br>
Submitted as part of the Tredence AI Engineering Internship Coding Assignment.
</p>
