#including packages
from langchain_community.llms import Ollama
import streamlit as st 
from langchain_core.prompts import ChatPromptTemplate 
from langchain_core.output_parsers import StrOutputParser

#creating propmts
prompt = ChatPromptTemplate.from_messages(
    [
        ("system","You are helpfull assistant. please respond to the question asked"),
        ("user","Question:{question}")
    ]
)

#frontend UI Design using Streamlit framework
st.title("My GPT")
input_text = st.text_input("Ask your question")

# ollama model integration
llm = Ollama(model="gemma2:2b")# step1
Output_Parser = StrOutputParser()# step2
chain = prompt | llm | Output_Parser

#input validation
if input_text:
 st.write(chain.invoke({"question":input_text}))