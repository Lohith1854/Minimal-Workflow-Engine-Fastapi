from typing import Dict, Any, Callable, Optional
from pydantic import BaseModel

class Node(BaseModel):
    name: str
    fn_name: str
    next: Optional[str] = None
    condition: Optional[dict] = None  # simple condition dict e.g. {"key":"quality_score","op":">=","value":80}
    loop: Optional[dict] = None  # e.g. {"cond_key":"quality_score","op":"<","value":80,"goto":"improve"}

class Graph(BaseModel):
    id: str
    nodes: Dict[str, Node]
    edges: Dict[str,str] = {}
 