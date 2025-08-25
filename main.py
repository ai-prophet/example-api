from typing import List, Optional
import time
import json
from fastapi import FastAPI, HTTPException, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from pydantic import BaseModel

# Pydantic models for OpenAI compatibility
class ChatMessage(BaseModel):
    role: str
    content: str

class ChatCompletionRequest(BaseModel):
    model: str = "mock-gpt-model" # this goes in the onboarding field "Model Name"
    messages: List[ChatMessage] 
    max_tokens: Optional[int] = 512
    temperature: Optional[float] = 0.1
    stream: Optional[bool] = False

app = FastAPI(title="Mock OpenAI-compatible API for ProphetArena Onboarding")

security = HTTPBearer()

# Mock valid token (in production, this would be validated against db or similar)
VALID_TOKEN = "mock-bearer-token-12345"

def verify_token(credentials: HTTPAuthorizationCredentials = Depends(security)):
    """Basic verification of bearer token"""
    if credentials.credentials != VALID_TOKEN:
        raise HTTPException(
            status_code=401,
            detail="Invalid authentication token",
            headers={"WWW-Authenticate": "Bearer"}
        )
    return credentials.credentials


@app.post("/chat/completions")
def chat_completions(request: ChatCompletionRequest, token: str = Depends(verify_token)):
    """
    OpenAI-compatible chat completions endpoint.
    """
    
    # You can access the input chat prompt with request.messages (a list of ChatMessage objects)
    # In this example we produce fake data. Replace the lines below with a call to your model.
   
    # This is mock prediction data, the prophet arena prompt will instruct the model to return this 
    # data in the same format. Delete this and replace with a call to your model.
    prediction_json = {
        "probabilities": {
            "0": 0.05,
            "1": 0.10,
            "2": 0.15,
            "3": 0.25,
            "4": 0.20,
            "5": 0.15,
            "6 or above": 0.10
        },
        "rationale": """Based on the provided sources, there is significant momentum building around cryptocurrency reserves globally. The sources indicate:

1. Multiple governments are already exploring digital asset regulations and reserve strategies
2. The U.S. has concrete proposals from political leaders for national Bitcoin reserves
3. Individual states like Texas, Pennsylvania, and Ohio are pursuing state-level reserves
4. Countries across five continents (including Czechia, Brazil, Russia, and Switzerland) are evaluating Bitcoin reserves

Given this widespread interest and the specific initiatives already underway, I estimate a moderate to high probability that 3-4 countries will successfully create crypto reserves this year, with some possibility of higher numbers due to the accelerating trend."""
    }
    response_content = json.dumps(prediction_json, indent=2)
    

    return {
        "id": "chatcmpl-mock-123",
        "object": "chat.completion",
        "created": int(time.time()),
        "model": request.model,
        "choices": [{
            "index": 0,
            "message": ChatMessage(role="assistant", content=response_content),
            "finish_reason": "stop"
        }],
        "usage": {
            "prompt_tokens": 100,
            "completion_tokens": 50,
            "total_tokens": 150
        }
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001) 