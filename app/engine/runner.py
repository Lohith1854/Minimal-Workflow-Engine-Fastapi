import asyncio
from typing import Dict, Any, List
from .graph import Graph,Node
from .tools import get_tool


RUNS: Dict[str, Dict] = {}

def eval_cond(state:Dict[str,Any],cond:Dict)->bool:
    if not cond: return False
    key=cond.get("key")
    op=cond.get("op")
    val=cond.get("value")
    cur=state.get(key)
    if op=="<": return cur < val
    if op==">": return cur > val
    if op==">=": return cur >= val
    if op=="<=": return cur <= val
    if op=="==": return cur == val
    return False

async def run_graph(graph:Graph,initial_state:Dict[str,Any],run_id:str):
    state = dict(initial_state)
    log:List[str]=[]
    
    if graph.nodes:
        current = next(iter(graph.nodes.values())).name
    else:
        RUNS[run_id] = {"state":state,"log":["empty graph"],"done":True}
        return RUNS[run_id]

    RUNS[run_id] = {"state":state,"log":log,"done":False}
    steps = 0
    while current and steps < 1000:
        steps += 1
        node = graph.nodes[current]
        log.append(f"running {node.name}")
        
        fn = get_tool(node.fn_name)
        if not fn:
            log.append(f"missing tool {node.fn_name}")
            break
        
        if asyncio.iscoroutinefunction(fn):
            out = await fn(state)
        else:
            out = fn(state)
            if asyncio.iscoroutine(out):
                out = await out
        if isinstance(out, dict):
            state.update(out)
        RUNS[run_id]["state"] = dict(state)
        RUNS[run_id]["log"] = list(log)

        
        if node.loop:
            if eval_cond(state,{"key":node.loop["cond_key"],"op":node.loop["op"],"value":node.loop["value"]}):
                
                current = node.loop.get("goto", node.next)
                log.append(f"loop -> {current}")
                continue

        
        if node.condition:
            if eval_cond(state,node.condition):
                current = node.next or None
            else:
                
                current = graph.edges.get(node.name)
        else:
            current = node.next

        if current is None:
            log.append("workflow ended")
            break

    RUNS[run_id]["state"] = dict(state)
    RUNS[run_id]["log"] = list(log)
    RUNS[run_id]["done"] = True
    return RUNS[run_id]

def get_run(run_id:str):
    return RUNS.get(run_id,{"state":{},"log":[],"done":False})
