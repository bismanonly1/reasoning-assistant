from langchain_core.prompts import PromptTemplate
from langchain_community.llms import Ollama
from tools.calculator import calculate
from langchain_experimental.tools import PythonREPLTool
from langchain_community.utilities.google_serper import GoogleSerperAPIWrapper

llm = Ollama(model="llama3")
python_tool = PythonREPLTool()
search_tool = GoogleSerperAPIWrapper(serper_api_key="9c9a8b804244c3adc5ebff502bbe9fa113b3328f58f85c294d3a0acdf7fe1184")

toolformer_template = PromptTemplate(
    input_variables=["question", "context", "tool_result"],
    template="""
You are an AI that can automatically decide when to use tools and answer question from the context of PDF provided.

Question: {question}

Context: {context}

If the question can be answered directly, provide the answer.
If the question requires a tool (calculator, PDF reader, API), suggest the  tool to use and then use the tool result.

Thought: Let's think step by step
Decision: [Tool to use or "No tool needed"]
Observation: [Tool result if applicable, or "N/A"]
Tool Result: {tool_result}
Final Answer:
"""
)

def run_toolformer(question, context):
    if not context:
        return "Sorry, no context provided to answer the question."
    
    reasoning = f"Processing question: {question}\n"
    tool_result = "N/A"

    if any(word in question.lower() for word in["code", "execute", "python"]):
        reasoning += "Detected code execution request, using Python REPL tool...\n"
        tool_result = python_tool.run(question)
        reasoning += f"Tool result: {tool_result}\n"

    elif any(word in question.lower() for word in ["current", "exchange rate", "convert", "currency"]):
        reasoning += "Detected currency conversion request, using search tool...\n"
        tool_result = search_tool.run(question)
        reasoning += f"Tool result: {tool_result}\n"

    elif any(word in question.lower() for word in ["calculate"]):
        reasoning += "Detected calculation request, using Calculator tool...\n"
        tool_result = calculate(question)
        reasoning += f"Tool result: {tool_result}\n"

    else:
        reasoning += "No specific tool needed. Proceding with LLM answer only..\n"
        
    reasoning += f"final tool result used: {tool_result}\n"

    prompt = toolformer_template.format(question=question, 
                                        tool_result=tool_result, 
                                        context=context,
                                        reasoning=reasoning)
    response = llm.invoke(prompt)
    return response