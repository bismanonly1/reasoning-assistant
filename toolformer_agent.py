from langchain_core.prompts import PromptTemplate
from langchain_community.llms import Ollama
from tools.pdf_reader import read_pdf
from tools.calculator import calculate

llm = Ollama(model="llama3")

toolformer_template = PromptTemplate(
    input_variables=["question"],
    template="""
You are an AI that can automatically decide when to use tools,

Question: {question}

If the question can be answered directly, provide the answer.
If the question requires a tool (calculator, PDF reader, API), suggest the  tool to use and then use the tool result.

Thought: Let's think step by step
Decision: [Tool to use or "No tool needed"]
Observation: [Tool result if applicable, or "N/A"]
Tool Result: {tool_result}
Final Answer:
"""
)

def run_toolformer(question):
    tool_result = "N/A"

    if any(op in question for op in ["+", "-", "*", "/", "times", "divided by"]):
        expression = question.replace("times", "*").replace("divided by", "/")
        tool_result = str(calculate(expression))

    prompt = toolformer_template.format(question=question, tool_result=tool_result)
    response = llm.invoke(prompt)
    return response