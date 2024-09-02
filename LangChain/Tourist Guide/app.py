from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import streamlit as st
import os
from langchain.schema import BaseOutputParser
from langchain.prompts.chat import ChatPromptTemplate
from langchain.chains import SequentialChain
import re


load_dotenv() #takes the environment variable from .env

# Defining the Output Parser for a structured Output
class parser(BaseOutputParser):
    def parse(self, output):
        # Step 1: Split the output into lines
        lines = output.strip().split('\n')
        # Step 2: Clean each line
        cleaned_lines = []
        for line in lines:
            # Remove leading numbers and extra quotes if they exist
            cleaned_line = re.sub(r'^\d+:\s*["\']?(.*?)["\']?$', r'\1', line)
            # Only add non-empty lines
            if cleaned_line:
                cleaned_lines.append(cleaned_line)
        
        # Step 3: Join the cleaned lines into a single string
        cleaned_output = '\n'.join(cleaned_lines)
        return cleaned_output

# define the model to get response
def model_response(prompt):
    llm = ChatGoogleGenerativeAI(google_api_key=os.getenv('GOOGLE_API_KEY'),model="gemini-1.5-flash")
    system_template="You're a tourist guide, you help people suggest the best destinations to visit. Always suggest the top five places"
    human_template="{prompt}"
    # initializing the prompt
    chatprompt=ChatPromptTemplate.from_messages([
        ('system',system_template),
        ('human',human_template)
    ])
    chain=chatprompt|llm|parser()
    response=chain.invoke(prompt)
    return response


# -------------------------------------------------------------------------
# Initialize streamlit
st.set_page_config(page_title="Tourist Guide to Find the Best Destinations")
st.header("Langchain based Tourist Guide")

# Get user input
input=st.text_input("Enter your location",key="input")
button=st.button("Get Places!")

if button:
    if input=="":
        st.error("Please enter your location")
    else:
        # Get response from model
        response=model_response(input)
        st.subheader("Response from the ChatBot")
        st.write(response)