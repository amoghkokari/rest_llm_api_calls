import textwrap

from all_models import getAI

def get_parsed_response(request):

    print(request)

    # get llm response
    llm_response = getAI(request.model, request.api_key, request.prompt)

    formatted_text = textwrap.indent(llm_response, prefix="")

    # Parse the response from the LLM
    return formatted_text