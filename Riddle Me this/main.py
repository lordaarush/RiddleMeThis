import streamlit as st
import langchain_helper
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain_community.llms import HuggingFaceEndpoint
import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()
os.environ["HUGGINGFACEHUB_API_TOKEN"] = os.getenv("HF_KEY")

# Initialize Hugging Face LLM
llm = HuggingFaceEndpoint(repo_id="google/gemma-1.1-7b-it")

# Define the prompt template
prompt_template_name = PromptTemplate(
    input_variables=['theme'],
    template="Give me 1 and only 1 riddle to solve with the following theme: {theme}. Make sure the answer is not the theme itself but something similar to and something with higher correlation to the theme provided. Return a simple hint and also the answer, after writing down the riddle, in separate lines. For reference here is what your response should look like, return a dictionary like this :-riddle:write the riddle here, hint: write the hint here, answer: write the answer here)"
)

# Initialize the LLMChain with the Hugging Face model and prompt template
chain = LLMChain(llm=llm, prompt=prompt_template_name)

# Streamlit UI components
st.title("Riddle Solver")

# Get the user's theme input
theme = st.text_input("Enter a theme for the riddle (e.g., halloween, america, nature):")

if theme:
    # Generate the riddle based on the theme
    response = chain.run(theme)

    # Use langchain_helper to extract the riddle, hint, and answer
    riddle_data = langchain_helper.extract_riddle_parts(response)

    # Display the riddle
    st.header("Riddle:")
    st.write(riddle_data['riddle'])

    # User input for answer guess
    user_guess = st.text_input("What is your guess?")

    # Hint button
    if st.button("Get Hint"):
        st.write("**Hint:**", riddle_data['hint'])

    # Reveal answer button
    if st.button("Reveal Answer"):
        st.write("**Answer:**", riddle_data['answer'])

    # Check if user's guess is correct
    if user_guess:
        if user_guess.strip().lower() == riddle_data['answer'].lower():
            st.success("Correct! Well done!")
        else:
            st.error("Incorrect. Try again or click 'Reveal Answer' for the correct solution.")
