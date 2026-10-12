import os
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import JsonOutputParser
from schemas import SupportTicket

# Initialize the LLM (Requires OPENAI_API_KEY in environment variables)
# Note: In a real enterprise environment, this can be swapped to IBM Granite or Watsonx
llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)

# Initialize the Output Parser using the Pydantic schema we created in File 1
parser = JsonOutputParser(pydantic_object=SupportTicket)

# Define the Prompt Template for extraction
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are an expert enterprise support ticket classifier. "
               "Analyze the following conversation history between a customer and a support agent. "
               "Extract the core issue and format your response strictly matching the provided JSON schema.\n\n"
               "{format_instructions}"),
    ("human", "Conversation History:\n{chat_history}\n\nExtract and classify this ticket.")
])

# Build the LCEL (LangChain Expression Language) Chain
# Data flows from the prompt -> to the model -> to the JSON parser
ticket_extraction_chain = prompt | llm | parser

def extract_ticket_data(chat_history: str) -> dict:
    """
    Executes the pipeline to extract structured JSON from the raw chat history.
    """
    return ticket_extraction_chain.invoke({
        "chat_history": chat_history,
        "format_instructions": parser.get_format_instructions()
    })
