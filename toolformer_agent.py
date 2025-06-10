from langchain_core.prompts import PromptTemplate
from langchain_community.llms import Ollama

llm = Ollama(model="llama3")

toolformer_template = PromptTemplate(
    input_variables=["question"],
    template="""
You are an AI that can automatically decide when to use tools,

Question: {question}

If the question can be answered directly, provide the answer."
If the question requires a tool (calculator, PDF reader, API), suggest the tool to use.

Thought: Let's think step by step
Decision: [Tool to use or "No tool needed"]
Observation: [Tool result if applicable, or "N/A"]
Final Answer:
"""
)

def run_toolformer(question):
    prompt = toolformer_template.format(question=question)
    response = llm.invoke(prompt)
    return response