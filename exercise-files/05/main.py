from langchain_community.document_loaders import TextLoader
from langchain_openai import OpenAIEmbeddings
from langchain_openai import ChatOpenAI
from langchain_text_splitters import CharacterTextSplitter
from langchain_core.output_parsers.openai_tools import PydanticToolsParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_openai import ChatOpenAI
from langchain_community.vectorstores import Chroma
from typing import List, Optional
from langchain_core.pydantic_v1 import BaseModel, Field
from langchain import hub
from dotenv import load_dotenv

load_dotenv()

llm = ChatOpenAI(temperature=0)


# Prompt with Query analysis

# Create Index & Connect to datasource

# Retrieval with Query analysis