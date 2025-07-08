from langchain_core.prompts import PromptTemplate
from langchain_ollama import OllamaLLM

llm = OllamaLLM(model = "llama3")

react_template = PromptTemplate(
    input_variables=["questions", "context"],
    template="""
You are an AI that can reason and use tools if needed and use the provided PDF content to answer the question.

Question: {question}

Conext: {context}
Reasoning + Action:

Thought: Let's think about this step by step.
Action: [describe the tool you would use, if needed]
Observation: [stimulate the tool result here, or say "no tool neede"]
Final Answer:
"""
)

def run_react(question, context):
    if not context:
        return "Sorry, no context provided to answer the question."
    prompt = react_template.format(question=question, context=context)
    response = llm.invoke(prompt)
    return response