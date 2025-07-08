from langgraph.graph import StateGraph, END
from typing import TypedDict, Annotated
from tools.pdf_reader import read_pdf

from cot_agent import run_cot
from react_agent import run_react
from toolformer_agent import run_toolformer
from camel_agent import run_camel

class MyState(TypedDict):
    question: Annotated[str, "input"]
    role: Annotated[str, "input"]
    cot_result: str
    react_result: str
    toolformer_result: str
    camel_result: str
    pdf_text: Annotated[str, "input"]
    camel_critique: str
    action_needed: str


def cot_step(state: MyState):
    question = state["question"]
    pdf_text = state.get("pdf_text", "")
    cot_result = run_cot(question, pdf_text)
    state["cot_result"] = cot_result
    return state

def camel_critique_step(state: MyState):
    cot_output = state["cot_result"]
    context = state["pdf_text"]
    critique = run_camel("Critic", f"Critique this reasoning: {cot_output}", context)
    state["camel_critique"] = critique
    if "missing" in critique.lower() or "weak" in critique.lower():
        state["action_needed"] = "tool_check"
    else:
        state["action_needed"] = "proceed"
    return state

def router_step(state: MyState):
    if state["action_needed"] == "tool_check":
        return {"next_step": "tool check"}
    else:
        return {"next_step": "proceed"}

def toolformer_step(state: MyState):
    question = state["question"]
    context = state.get("pdf_text", "")
    toolformer_result = run_toolformer(question, context)
    state["toolformer_result"] = toolformer_result
    return state
    
def react_step(state: MyState):
    question = state["question"]
    pdf_text = state.get("pdf_text", "")
    react_result = run_react(question, pdf_text)
    state["react_result"] = react_result
    return state


def camel_step(state: MyState):
    question = state["question"]
    pdf_text = state.get("pdf_text", "")
    role = state.get("role", "Scientist")
    camel_result = run_camel(role, question, pdf_text)
    state["camel_result"] = camel_result
    return state

    
graph = StateGraph(state_schema=MyState)

graph.add_node("Chain-of-Thought", cot_step)
graph.add_node("Camel Critique", camel_critique_step)
graph.add_node("Router", router_step)
graph.add_node("Toolformer", toolformer_step)
graph.add_node("ReAct", react_step)
graph.add_node("Camel Agent", camel_step)

graph.set_entry_point("Chain-of-Thought")

graph.add_edge("Chain-of-Thought", "Camel Critique")
graph.add_edge("Camel Critique", "Router")
graph.add_conditional_edges(
    "Router",
    lambda state: state["next_step"],
    {
        "tool check": "Toolformer",
        "proceed": "Camel Agent"
    }
)
graph.add_edge("Toolformer", "ReAct")
graph.add_edge("ReAct", "Camel Agent")
graph.add_edge("Camel Agent", END)

app = graph.compile()

def run_langgraph_flow(question, role="Scientist", pdf_path=None):
    pdf_text = read_pdf(pdf_path) if pdf_path else ""
    initial_state = {
        "question": question,
        "role": role,
        "pdf_text": pdf_text,
        "cot_result": "",
        "react_result": "",
        "toolformer_result": "",
        "camel_result": "",
        "camel_critique": "",
        "action_needed": ""
    }

    for state in app.stream(initial_state):
        print(f"\n=== State update ===")
        print(state)

    return state