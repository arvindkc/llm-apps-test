import json
import streamlit as st
from langchain.chains import LLMChain
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from third_parties.linkedin import scrape_linkedin_profile


from dotenv import load_dotenv
import pprint
load_dotenv()



if __name__ == '__main__':
    linked_in_profile_url = st.text_input("Enter the linkedin profile url", "https://www.linkedin.com/in/arvindkc/")
    # linked_in_profile_url = "https://www.linkedin.com/in/arvindkc/"
    linkedin_data = scrape_linkedin_profile(linkedin_profile_url=linked_in_profile_url)
    #linkedin_data_str = json.dumps(linkedin_data, indent=4)
    # print(linkedin_data_str)
    # print(os.getenv('OPENAI_API_KEY'))
    
    summary_template = """ 
    given the linked information {information} about a person I want you to create:
    1. A short summary
    2. A summary of their key technical skills
    3. Years of experience
    4. Companies they have worked for
    """

    summary_prompt_template = PromptTemplate(
        input_variables=["information"], template=summary_template
    )

    llm =ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")

    chain = LLMChain(llm=llm, prompt=summary_prompt_template)
    response = chain.invoke(input={"information":linkedin_data})
    response_str = json.dumps(response["text"], indent=4)
    response_dict = json.loads(response_str)
    print(response_dict)

    st.header("Linkedin Profile Summary", divider='blue')
    st.write('Showing linkedin profile summary for the profile: ', linked_in_profile_url)
    st.write(response_dict)