from langchain_core.prompts import PromptTemplate
from langchain_community.llms import Ollama

llm = Ollama(model="llama3")

camel_template = PromptTemplate(
    input_variables=["question"],
    template="""
You are acting as a {role}. Please answer the following question with that role's perspective.

Question: {question}

Answer as {role}:
"""
)

def run_camel(role, question):
    prompt = camel_template.format(role=role, question=question)
    response=llm.invoke(prompt)
    return response