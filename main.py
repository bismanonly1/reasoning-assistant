from cot_agent import run_cot

if __name__ == "__main__":
    question = input("Enter your question: ")

    print("\n=== Chain-of-Thought ==")
    cot_result = run_cot(question)
    print(cot_result)
