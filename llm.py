import os
from langchain.chat_models import ChatOpenAI
from langchain import PromptTemplate, LLMChain
from langchain.prompts.chat import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    AIMessagePromptTemplate,
    HumanMessagePromptTemplate,
)
from langchain.schema import (
    AIMessage,
    HumanMessage,
    SystemMessage
)

def cl_generator(resume, job_desc, openai_key, temp):
    # Initialize the ChatOpenAI model for generating text
    chat = ChatOpenAI(temperature=temp, openai_api_key=openai_key)

    # Set up the template for the system message
    system_message_template = "You are a student that has to write a cover letter to apply for a job. "
    system_message_prompt = SystemMessagePromptTemplate.from_template(system_message_template)

    # Set up the template for the human message
    human_template = "This is your resume:\n{resume}\nThis is the job description:\n{job_desc}"
    human_message_prompt = HumanMessagePromptTemplate.from_template(human_template)

    # Set up the chat prompt template with system and human messages
    chat_prompt = ChatPromptTemplate.from_messages([system_message_prompt, human_message_prompt])

    # Create the LLMChain with the ChatOpenAI model and chat prompt
    chain = LLMChain(llm=chat, prompt=chat_prompt)

    # Provide the resume and job description as inputs to the chat
    input_data = {"resume": resume, "job_desc": job_desc}

    # Generate the cover letter by running the LLMChain
    return chain.run(input_data)
