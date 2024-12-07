"""from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chains import SequentialChain
from langchain_community.llms import HuggingFaceEndpoint
from langchain_community.chat_models.huggingface import ChatHuggingFace
import os
from dotenv import load_dotenv
import re


load_dotenv()
os.environ["HUGGINGFACEHUB_API_TOKEN"] = os.getenv("HF_KEY")



llm = HuggingFaceEndpoint(repo_id="google/gemma-1.1-7b-it")     

prompt_template_name = PromptTemplate(
    input_variables=['theme'],
    template="Give me 1 and only 1 riddle to solve with the following theme: {theme}. Make sure the answer is not the theme itself but someting similar to and something with higher correlation to the theme provided. Return a simple hint and also the answer, after writing down the riddle, in seperate lines. For reference here is what your response should look like, return a dictionary like this :-riddle:write the riddle here, hint: write the hint here, answer: write the answer here)"
)

#prompt_template_name.format(theme="halloween")
chain = LLMChain(llm=llm,prompt=prompt_template_name)
#r = chain.run("america")
"""
import re

def extract_riddle_parts(text):
    # Define patterns for riddle, hint, and answer
    riddle_pattern = r"\*\*Riddle:\*\*\n(.+?)(?:\n\n|\Z)"
    hint_pattern = r"\*\*Hint:\*\*\n(.+?)(?:\n\n|\Z)"
    answer_pattern = r"\*\*Answer:\*\*\n(.+?)(?:\n\n|\Z)"
    
    # Extract each part using regular expressions
    riddle_match = re.search(riddle_pattern, text, re.DOTALL)
    hint_match = re.search(hint_pattern, text, re.DOTALL)
    answer_match = re.search(answer_pattern, text, re.DOTALL)
    
    # Get the text or set None if not found
    riddle = riddle_match.group(1).strip() if riddle_match else None
    hint = hint_match.group(1).strip() if hint_match else None
    answer = answer_match.group(1).strip() if answer_match else None
    
    # Return the dictionary with the extracted values
    return {
        "riddle": riddle,
        "hint": hint,
        "answer": answer
    }


#result = extract_riddle_parts(r)
#print(result)