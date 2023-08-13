"""main.py
Python FastAPI Auth0 integration example
"""

from fastapi import Depends, FastAPI, status, Response
from fastapi.security import HTTPBearer 
import uvicorn

from utils import VerifyToken

# Scheme for the Authorization header
token_auth_scheme = HTTPBearer()

# Creates app instance
app = FastAPI()


@app.get("/")
def root():

    return {"msg": "Hello World"}
 
@app.get("/api/public")
def public():
    """No access token required to access this route"""

    result = {
        "status": "success",
        "msg": ("Hello Status Code 0 👀")
    }
    return result


@app.get("/api/private")
def private(response: Response, token: str = Depends(token_auth_scheme)):
    """A valid access token is required to access this route"""
    
    result = VerifyToken(token.credentials).verify()

    if result.get("status"):
       response.status_code = status.HTTP_400_BAD_REQUEST
       return result

    response = {
        "status": "success",
        "msg": ("Yay! You made an Authenticated request.")
    }
    
    return response


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)