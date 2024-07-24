# Import necessary modules and functions
from prompt_templates import memory_prompt_template
from langchain.chains import StuffDocumnetsChain, LLMChain, ConversationalRetrivalChain
from langachain.embeddings import HuggingFaceInstructEmbeddings
from langchain.memory import ConversationBufferMemory
from langchain.prompts import PromptTemplate
from langchain.llms import CTransformers
from langchain.vectorstores import Chroma
import chromadb
import yaml

# Load configuration from a YAML file
with open("config.yml", "r") as f:
    config = yaml.safe_load(f)

# Function to create a large language model (LLM) using CTransformers
def create_llm(model_path = config["model_path"]["large"], model_type = config["model_type"]):
    llm = CTransformers(model_path, model_type)
    return llm

# Function to create embeddings using HuggingFaceInstructEmbeddings
def create_embeddings(embeddings_path = config["embeddings_path"]):
    return HuggingFaceInstructEmbeddings(embeddings_path)

# Function to create a conversation buffer memory
def create_chat_memory(chat_history):
    return ConversationBufferMemory(memory_key="history", chat_memory=chat_history, k=3)

# Function to create a prompt from a given template
def create_prompt_from_template(template):
    return PromptTemplate.from_template(template)

# Function to create an LLM chain with a given LLM, prompt, and memory
def create_llm_chain(llm, chat_prompt, memory):
    return LLMChain(llm, chat_prompt, memory)

# Function to load a normal chat chain
def load_normal_chain(chat_history):
    return chatChain(chat_history)

# Chat chain class definition
class chatChain:
    
    def __init__(self, chat_history, model_path = config["model_path"]["large"], model_type = config["model_type"]):
        self.memory = create_chat_memory(chat_history)
        llm = create_llm(model_path, model_type)
        chat_prompt = create_prompt_from_template(memory_prompt_template)
        self.llm_chain = create_llm_chain(llm, chat_prompt, self.memory)

    # Method to run the chat chain with user input
    def run(self, user_input):
        return self.llm_chain.run(human_input = user_input, history=self.memory.chat_memory.messages, stop=["Human:"])
