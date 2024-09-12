import os
import re
from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAI
from langchain.prompts.chat import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema import BaseOutputParser
import streamlit as st

load_dotenv()
GOOGLE_API_KEY=os.getenv("GOOGLE_API_KEY")

def response(prompt,style):
    system_template="""You're an English Literature Expert who specializes in poetry writing. 
                    Write a poetry of the highest standard based following the rules of poetry on the given title: 
                    <title>
                    {prompt}
                    </title>
                    The style of the writing should replicate the style of {style}"""
    human_temmplate="{prompt},  {style}"
    prompt_template=ChatPromptTemplate.from_messages(
        [
            ("system",system_template),
            ("human",human_temmplate)
        ]
    )
    llm=GoogleGenerativeAI(model='models/gemini-1.5-flash',temperature=0.8,google_api_key=os.getenv("GOOGLE_API_KEY"))
    chain = prompt_template|llm|StrOutputParser()
    result=chain.invoke({"prompt": prompt, "style": style})
        # Ensure the result is a string and return it
    if isinstance(result, str):
        return result
    else:
        return str(result)

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

# print(response("Happiness","Kafka"))

st.set_page_config("Fictional Poetry Writer")
st.header("fictional poetry by your favourite authors")

title=st.text_input("Enter the title",key="title")
style=st.selectbox("Select the style",["Kafka","Shakespeare","Hemingway","Edgar Allen Poe","Sylvia Plath","Mary Wollstonecraft", "Emily Dickinson"])
button=st.button("Get Poem!")

if button:
    if title=="":
        st.error("Please enter a Title")
    else:
        # Get response from model
        result=response(prompt=title,style=style)
        st.subheader("Response from the Author")
        # st.write("Debug: Raw Response Type:", type(result))  # Debugging: Check response type
        # st.write("Debug: Raw Response Content:", result)  # Debugging: Check raw content
        st.write(result)
        # try:
        #     st.subheader(f"Poetry in the style of {style}")
        #     st.write(response(title, style) )  # Display the result in Streamlit
        # except Exception as e:
        #     st.error(f"Error generating the poem: {e}")


