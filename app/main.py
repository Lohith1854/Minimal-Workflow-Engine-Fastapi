from fastapi import FastAPI,HTTPException
from pydantic import BaseModel
import uuid
from .engine.graph import Graph,Node
from .engine.runner import run_graph,get_run
from .workflows import code_review

app = FastAPI(title="Minimal Workflow Engine")


GRAPHS = {}
RUN_STORE = {}

class CreateGraphReq(BaseModel):
    id: str = None
    nodes: dict

class RunReq(BaseModel):
    graph_id: str
    initial_state: dict = {}

@app.post("/graph/create")
def create_graph(req:CreateGraphReq):
    gid = req.id or str(uuid.uuid4())
    nodes = {}
    for name,node in req.nodes.items():
        nodes[name] = Node(name=name,**node)
    graph = Graph(id=gid,nodes=nodes)
    GRAPHS[gid] = graph
    return {"graph_id":gid}

@app.post("/graph/run")
async def run(req:RunReq):
    graph = GRAPHS.get(req.graph_id)
    if not graph:
        raise HTTPException(status_code=404,detail="graph not found")
    run_id = str(uuid.uuid4())
    
    result = await run_graph(graph, req.initial_state, run_id)
    return {"run_id": run_id, "final_state": result["state"], "log": result["log"]}

@app.get("/graph/state/{run_id}")
def state(run_id: str):
    r = get_run(run_id)
    return r
