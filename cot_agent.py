from langchain_core.prompts import PromptTemplate
from langchain_community.llms import Ollama

llm = Ollama(model="llama3")

cot_template = PromptTemplate(
    input_variables=["question"],
    template="""
    You are a thoughtful AI. Please think step by step to answerthe following question:

    Question: {question}

    Let's think step by step:
    """
)

def run_cot(question):
    prompt = cot_template.format(question=question)
    response = llm.invoke(prompt)
    return response