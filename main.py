from cot_agent import run_cot
from react_agent import run_react
from toolformer_agent import run_toolformer
from camel_agent import run_camel
from langgraph_flow import run_langgraph_flow

if __name__ == "__main__":
    question = input("Enter your question: ")
    role = input("Enter role for Camel Agent (default: Scientist): ") or "Scientist"
    pdf_path = "/Users/bismansingh/reasoning-assistant/docs/tech_lab_report.pdf"

    print("\n=== Chain-of-Thought ===")
    cot_result = run_cot(question, pdf_path)
    print(cot_result)

    print("\n=== React Agent ===")
    react_result = run_react(question, pdf_path)
    print(react_result)

    print("\n=== Toolformer Agent ===")
    toolformer_result = run_toolformer(question, pdf_path)
    print(toolformer_result)

    print("\n=== Camel Agent (Scientist role) ===")
    camel_result = run_camel("Scientist", question, pdf_path)
    print(camel_result)
    
    print("\n=== Full Langgraph Reasoning Bot Flow ===")
    run_langgraph_flow(question, role, pdf_path)