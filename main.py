from cot_agent import run_cot
from react_agent import run_react

if __name__ == "__main__":
    question = input("Enter your question: ")

    print("\n=== Chain-of-Thought ==")
    cot_result = run_cot(question)
    print(cot_result)

    print("\n=== React Agent ===")
    react_result = run_react(question)
    print(react_result)
