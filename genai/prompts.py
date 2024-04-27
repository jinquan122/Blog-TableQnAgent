from datetime import datetime
from llama_index.core.llms import ChatMessage

## The prompt to use for generating the structured filter from the current available items in category and merchant
structured_filter_prompt='''
    As a Natural Language Expert with a strong background in SQL within the banking transaction industry, your task involves processing a specific query. Using the provided lists of categories and merchants, you will extract relevant items from the query based on these lists.

    Please follow the instructions below:

    1. Review the Query provided.
    2. Choose items from the Category List and Merchant List which are identified as relevant categories or merchants mentioned in the Query.
    3. Ensure that the category and merchant names you use match exactly with the names listed in the Category List and Merchant List.
    4. Ensure your response aligns with the format instructions provided.

    Details:

    - Category List: {category_list}
    - Merchant List: {merchant_list}

    Query to Process:

    {query}

    Format Instructions:

    {format_instructions}
    '''

def init_sql_prompt(filtered_structured_object:dict, query:str) -> str:
    '''
    Generate prompt for generating SQL query.

    Args:
    - filtered_structured_object (dict): Filtered structured object containing category and merchant if items are found matching with query.
    - query (str): User question.
    
    Returns:
    - str: SQL generation Prompt.
    '''
    prompt = f'''You are tasked with generating DuckDB SQL code based on provided details. Please follow the instructions and information given below:

    - **Here are the specific rules you'll need to accomplish this:**
                        
       1. Generate a single DuckDB SQL query as the output, end the DuckDB SQL with a semicolon.    

    - **Table Name:** The name of the table you will work with is `df`.

    - **Column Names and Types:** The table includes the following columns with their respective data types:
    - `client_id`: Integer
    - `bank_id`: Integer
    - `account_id`: Integer
    - `transaction_id`: Integer
    - `transaction_date`: Date (formatted as Timestamp 'yyyy-MM-dd')
    - `transaction_description`: String (with a maximum length of 200 characters)
    - `amount`: Float
    - `category`: String (with a maximum length of 200 characters)
    - `merchant`: String (with a maximum length of 200 characters)

    - **Filters:** You will also be given a list of conditions (referred to as a filter object) to apply to the SQL query. These conditions should be implemented in the `WHERE` clause of your SQL query.
    
    - **Filter Object:** {filtered_structured_object}

    - **Current Date:** {datetime.today()}

    - **Example Bad SQL query:** 
    SELECT SUM(amount) 
    FROM df 
    WHERE client_id = 6 
    AND category = 'Loans' 
    AND transaction_date >= DATE_TRUNC('month', CURRENT_TIMESTAMP - INTERVAL '10 month') 
    AND transaction_date <= CURRENT_TIMESTAMP;

    - **Example Good SQL query:**
    SELECT SUM(amount) 
    FROM df 
    WHERE client_id = 6 
    AND category = 'Loans' 
    AND transaction_date > '2023-06-25' 
    AND transaction_date <= '2024-04-25';
            
    - **Query:** {query}

    **end the DuckDB SQL with a semicolon**'''
    return prompt

def sythesizer_prompt(filtered_structured_object: dict, query: str, results: str):
    '''
    Generate prompt for synthesize results and questions.

    Args:
    - filtered_structured_object (dict): Filtered structured object containing category and merchant if items are found matching with query.
    - query (str): User question.
    - results (str): Pandas dataframe output.

    Returns:
    - str: Synthesizer Prompt.
    '''
    prompt = f'''
    Given an input question, synthesize a response from the query results. Strictly follow the rules when answering the query:

    Rules:
    1. Always provide a response to the input question. If the query results do not contain relevant information, reply with "No relevant information found."
    2. Use only the information from the query results to formulate your answer.
    3. Do not preface your answer with phrases like "based on information."
    4. Clearly state the criteria used to filter the information before answering.
    
    Filter: {filtered_structured_object}
    Query: {query}
    Pandas Output: {results}

    Format for the response:
    - End your response by specifying the filters applied, mentioning both the category and merchant involved. (Filtered by category: [category_name] and merchant: [merchant_name])
    '''
    return prompt

# def valid_sql_prompt(filtered_structured_object, init_sql, query):
#     prompt = f'''As an expert in DuckDB SQL, your task is to verify and, if necessary, revise a provided SQL query to ensure it conforms to DuckDB SQL standards and accurately reflects the user's data requirements. The process involves understanding the data the user aims to analyze, checking column availability, modifying the SELECT clause appropriately, performing any required mathematical operations, and producing a valid DuckDB SQL query.
                        
#     - **Here are the specific steps and information you'll need to accomplish this:**
                            
#     1. Interpret the data type or specific information the user wants to extract based on the given query.
#     2. Verify if the required data exists among the provided column names.
#     3. Incorporate the appropriate column(s) into the SELECT clause.
#     4. If needed, apply mathematical operations within the SELECT clause.
#     5. Generate a single DuckDB SQL query as the output, end the DuckDB SQL with a semicolon.
                                            
#     - **Table Name:** The name of the table you will work with is `df`.

#     - **Column Names and Types:** The table includes the following columns with their respective data types:
#     - `client_id`: Integer
#     - `bank_id`: Integer
#     - `account_id`: Integer
#     - `transaction_id`: Integer
#     - `transaction_date`: Date (formatted as Timestamp 'yyyy-MM-dd 00:00:00')
#     - `transaction_description`: String (with a maximum length of 200 characters)
#     - `amount`: Float
#     - `category`: String (with a maximum length of 200 characters)
#     - `merchant`: String (with a maximum length of 200 characters)

#     - **Filters:** You will also be given a list of conditions (referred to as a filter object) to apply to the SQL query. These conditions should be implemented in the `WHERE` clause of your SQL query.

#     - **Filter Object:** {filtered_structured_object}

#     - **SQL query:** {init_sql}

#     **Current Date:** {datetime.today()} 
                
#     **Query:** {query}

#     **Generate a single DuckDB SQL query as the output.**'''
#     return prompt