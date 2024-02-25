import streamlit as st
import json
from langchain.chains import LLMChain
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate

from dotenv import load_dotenv
load_dotenv()

st.header("Steamlit-ChatGPT example", divider='rainbow')

default_input_text = """

"""

input_text = st.text_area("Type your message here", height=50)

prompt_template = """
Given the input text {input_text}, Summarize it as if you were 
explaining it to a 5 year old.
"""

summary_prompt_template = PromptTemplate(
        input_variables=["input_text"], template=prompt_template
    )

llm =ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")

chain = LLMChain(llm=llm, prompt=summary_prompt_template)
response = chain.invoke(input={"input_text":input_text})
response_text = response["text"]
st.write(response_text)