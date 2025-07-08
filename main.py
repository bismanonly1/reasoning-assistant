from cot_agent import run_cot
from react_agent import run_react
from toolformer_agent import run_toolformer
from camel_agent import run_camel
from langgraph_flow import run_langgraph_flow
from tools.pdf_reader import read_pdf

if __name__ == "__main__":
    question = input("Enter your question: ")
    role = input("Enter role for Camel Agent (default: Scientist): ") or "Scientist"
    pdf_path = "/Users/bismansingh/reasoning-assistant/docs/tech_lab_report.pdf"
    pdf_text = read_pdf(pdf_path)

    print("\n=== Full Langgraph Reasoning Bot Flow ===")
    run_langgraph_flow(question, role, pdf_path)
    