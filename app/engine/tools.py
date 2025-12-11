from typing import Callable, Dict,Any

TOOL_REGISTRY: Dict[str,Callable] = {}

def register_tool(name:str,fn:Callable):
    TOOL_REGISTRY[name] = fn

def get_tool(name:str):
    return TOOL_REGISTRY.get(name)
