from langchain.output_parsers import ResponseSchema, StructuredOutputParser

def structured_output_parser() -> StructuredOutputParser:
    '''
    Creates a StructuredOutputParser instance for category and merchant list.

    Returns:
        StructuredOutputParser: The StructuredOutputParser instance.
    '''
    response_schemas = [
        ResponseSchema(
            name="category", 
            description="List of related categories found in the query.",
            type="list"
        ),
        ResponseSchema(
            name="merchant",
            description="List of merchant found in the query.",
            type="list"
        ),
    ]
    output_parser = StructuredOutputParser.from_response_schemas(response_schemas)
    return output_parser