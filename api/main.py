import uvicorn 
from at import app

if __name__ == "__main__":
    uvicorn.run("main:app", port=8080, host="0.0.0.0",reload = True)
    