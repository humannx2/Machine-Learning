import ast
from dotenv import load_dotenv
import os
from langchain_google_genai import GoogleGenerativeAI
from langchain.prompts.chat import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# Loading API
load_dotenv()
GOOGLE_API_KEY=os.getenv("GOOGLE_API_KEY")


# Defining Abstract Tree 
def extract(code):
    tree = ast.parse(code)
    functions=[node for node in tree.body if isinstance(node,ast.FunctionDef)]
    classes=[node for node in tree.body if isinstance(node,ast.ClassDef)]
    return functions,classes

# response function
def response(code):
    functions,classes=extract(code)
    # selecting one function from a list of functions
    for func in functions:
        func_name = func.name #extracting the name of the function
        args = [arg.arg for arg in func.args.args]
        system_template=f"""You are an AI Coding Assistant that writes documentation for the provided code, 
                            Write explaination about the function {func_name} and it's arguments {args} in the following code"""
        human_template=f"Function name: {func_name}, Arguments: {args}"
        prompt=ChatPromptTemplate.from_messages(
            [
                ("system",system_template),
                ("human",human_template)
            ]
        )  
        doc=generate(prompt,code)
        print(f"Function: {func_name}\nDocumentation:\n{doc}\n")

def generate(prompt,code_input):
    #  Defining the model
    llm=GoogleGenerativeAI(model='models/gemini-1.5-flash',temperature=0.8,google_api_key=os.getenv("GOOGLE_API_KEY"))
    # Generating the response
    chain=prompt|llm|StrOutputParser()
    # Invoke the chain to get the result
    try:
        result = chain.invoke({"input": code_input})
    except Exception as e:
        return f"Error generating documentation: {str(e)}"
    # Ensure the result is a string and return it
    if isinstance(result, str):
        return result
    else:
        return str(result)




# Example Code Input
code = """
def odd(n):
    if n%2==0:
        print("Number is even")
    else:
        print("Number is odd")

def hii(name):
    print (f"hello {name}")
"""

# Call the response function with the code
response(code)
