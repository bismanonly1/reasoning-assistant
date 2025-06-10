from langchain_core.prompts import PromptTemplate
from langchain_community.llms import Ollama

llm = Ollama(model = "llama3")

react_template = PromptTemplate(
    input_variables=["questions"],
    template="""
You are an AI that can reason and use tools if needed.

Question: {question"}

Reasoning + Action:

Thought: Let's think about this step by step.
Action: [describe the tool you would use, if needed]
Observation: [stimulate the tool result here, or say "no tool neede"]
Final Answer:
"""
)

def run_react(question):
    prompt = react_template.format(question=question)
    response = llm.invoke(prompt)
    return response