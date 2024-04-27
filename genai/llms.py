import torch
from llama_index.llms.huggingface import HuggingFaceLLM
from transformers import BitsAndBytesConfig
from langchain_google_genai import GoogleGenerativeAI
from google.generativeai.types import HarmCategory, HarmBlockThreshold
from langchain_groq import ChatGroq

def groq_llm():
    '''
    Initialize the Groq LLM.

    Returns:
        A Groq LLM.
    '''
    llm = ChatGroq(model_name="llama3-70b-8192", groq_api_key="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", temperature=0)
    return llm

safety_settings = {
            HarmCategory.HARM_CATEGORY_HATE_SPEECH: HarmBlockThreshold.BLOCK_NONE,
            HarmCategory.HARM_CATEGORY_HARASSMENT: HarmBlockThreshold.BLOCK_NONE,
            HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT: HarmBlockThreshold.BLOCK_NONE,
            HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: HarmBlockThreshold.BLOCK_NONE,
        }

def main_llm():
    '''
    Initialize the gemini-pro LLM.

    Returns:
        A gemini-pro LLM.
    '''
    llm = GoogleGenerativeAI(
            model="gemini-pro", 
            google_api_key="AIzaSyCCcHT_A9GdjtUNyd8HF6Bl9VDsR4aYITw",
            safety_settings=safety_settings
            )
    return llm

# def code_llm():
#     nf4_config = BitsAndBytesConfig(
#     load_in_4bit=True,
#     bnb_4bit_quant_type="nf4",
#     bnb_4bit_compute_dtype=torch.bfloat16
#     )


#     llm = HuggingFaceLLM(
#         context_window=4096,
#         max_new_tokens=2048,
#         generate_kwargs={"temperature": 0.1, "do_sample": True},
#         # query_wrapper_prompt=query_wrapper_prompt,
#         tokenizer_name='Qwen/CodeQwen1.5-7B-Chat',
#         model_name='Qwen/CodeQwen1.5-7B-Chat',
#         device_map="cuda",
#         # change these settings below depending on your GPU
#         # model_kwargs={"torch_dtype": torch.float16, "load_in_8bit": True},
#         model_kwargs={"quantization_config":nf4_config},
#         tokenizer_outputs_to_remove=["token_type_ids"]
#     )
#     return llm