from typing import Dict,Any
from ..engine.tools import register_tool

def extract_functions(state:Dict[str,Any]):
    
    state["functions"] = ["f1","f2","f3"]
    return {"extracted":True}

def check_complexity(state:Dict[str,Any]):
    
    state["complexities"] = {"f1":5,"f2":12,"f3":3}
    
    avg = sum(state["complexities"].values())/len(state["complexities"])
    
    quality = max(0,100 - int(avg*5))
    state["quality_score"] = quality
    return {"quality_score":quality}

def detect_issues(state:Dict[str,Any]):
    issues = []
    for f,c in state.get("complexities",{}).items():
        if c>10:
            issues.append({"fn":f,"issue":"high_complexity"})
    state["issues"] = issues
    return {"issues":issues}

def suggest_improvements(state:Dict[str,Any]):
    
    comp = state.get("complexities",{})
    for k in comp:
        comp[k] = max(1, comp[k]-4)
    state["complexities"]=comp
    
    avg = sum(comp.values())/len(comp)
    state["quality_score"] = max(0,100 - int(avg*5))
    return {"quality_score":state["quality_score"]}


register_tool("extract_functions", extract_functions)
register_tool("check_complexity", check_complexity)
register_tool("detect_issues", detect_issues)
register_tool("suggest_improvements", suggest_improvements)
