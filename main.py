from cot_agent import run_cot
from react_agent import run_react
from toolformer_agent import run_toolformer
from camel_agent import run_camel

if __name__ == "__main__":
    question = input("Enter your question: ")

    print("\n=== Chain-of-Thought ==")
    cot_result = run_cot(question)
    print(cot_result)

    print("\n=== React Agent ===")
    react_result = run_react(question)
    print(react_result)

    print("\n=== Toolformer Agent ===")
    toolformer_result = run_toolformer(question)
    print(toolformer_result)

    print("\n=== Camel Agent (Scientist role) ===")
    camel_result = run_camel("Scientist", question)
    print(camel_result)