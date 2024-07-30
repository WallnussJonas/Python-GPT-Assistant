from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

template = """
Answer the question below.
This is the chat history: {context}

Question: {question}

Answer:
"""

model = OllamaLLM(model="phi3")
prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model
output = chain.invoke({"context": "", "question": "What is the meaning of life?"})
print(output)