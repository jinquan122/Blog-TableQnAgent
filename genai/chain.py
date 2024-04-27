from langchain.prompts import PromptTemplate
from genai.prompts import structured_filter_prompt


def extract_structured_filter(output_parser, query:str, category_list:list, merchant_list:list, llm):
    '''
    Extracts category and merchant list from the response.

    Args:
        output_parser (StructuredOutputParser): The output parser.
        query (str): User question.
        category_list (list): List of categories.
        merchant_list (list): List of merchants.
        llm (BaseLanguageModel): The LLM.

    Returns:
        dict: The structured category and merchant list.
    '''
    format_instructions = output_parser.get_format_instructions()
    prompt = PromptTemplate(
        template=structured_filter_prompt,
        input_variables=["query", "category_list","merchant_list"],
        partial_variables={"format_instructions": format_instructions},
    )
    chain = prompt | llm | output_parser
    structured_object = chain.invoke({"query": query, "category_list":category_list, "merchant_list":merchant_list})
    return structured_object