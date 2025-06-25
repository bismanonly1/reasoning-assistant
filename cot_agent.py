from langchain_core.prompts import PromptTemplate
from langchain_community.llms import Ollama

llm = Ollama(model="llama3")

cot_template = PromptTemplate(
    input_variables=["question", "context"],
    template="""
    You are a highly logical assistant. The only source of truth is the following PDF context. You are not allowed to use prior knowledge or assumptions.

    Your job is to analyze the context step by step to answer the question clearly and accurately.

    Question: {question}

    Context: {context}

    Let's think step by step:
    """
)

def run_cot(question, context):
    if not context:
        return "Sorry, no context provided to answer the question."
    prompt = cot_template.format(question=question, context=context)
    response = llm.invoke(prompt)
    return str(response)