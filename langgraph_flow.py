from langgraph.graph import StateGraph, END
from typing import TypedDict
from langchain_core.messages import HumanMessage, AIMessage

from cot_agent import run_cot
from react_agent import run_react
from toolformer_agent import run_toolformer
from camel_agent import run_camel

class MyState(TypedDict):
    question: str
    role: str
    cot_result: str
    react_result: str
    toolformer_result: str
    camel_result: str

def cot_step(state: MyState):
    question = state["question"]
    cot_result = run_cot(question)
    state["cot_result"] = cot_result
    return state
    
def react_step(state: MyState):
    question = state["question"]
    react_result = run_react(question)
    state["react_result"] = react_result
    return state

def toolformer_step(state: MyState):
    question = state["question"]
    toolformer_result = run_toolformer(question)
    state["toolformer_result"] = toolformer_result
    return state

def camel_step(state: MyState):
    question = state["question"]
    role = state.get("role", "Scientist")
    camel_result = run_camel(role, question)
    state["camel_result"] = camel_result
    return state

graph = StateGraph(state_schema=MyState)

graph.add_node("Chain-of-Thought", cot_step)
graph.add_node("ReAct", react_step)
graph.add_node("Toolformer", toolformer_step)
graph.add_node("Camel Agent", camel_step)

graph.set_entry_point("Chain-of-Thought")

graph.add_edge("Chain-of-Thought", "ReAct")
graph.add_edge("ReAct", "Toolformer")
graph.add_edge("Toolformer", "Camel Agent")
graph.add_edge("Camel Agent", END)

app = graph.compile()

def run_langgraph_flow(question, role="Scientist"):
    state = {
        "question": question,
        "role": role
    }

    for state in app.stream(state):
        print(f"\n=== State update ===")
        print(state)

    return state