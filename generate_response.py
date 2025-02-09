from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from response_parser import get_parsed_response

# Create a router for the API
router = APIRouter()

class FieldsRequest(BaseModel):
    model: str
    api_key: str
    prompt: str

@router.post("/get_fields")
async def generate_response(request: FieldsRequest):
    try:
        # Call the LLM client to get a response
        parsed_response = get_parsed_response(request)

        return parsed_response

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))