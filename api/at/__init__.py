from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

__version__ = "0.0.1"

#Set Fast API App

app = FastAPI(
    title = "at-me Internal API",
    description = "at-me Internal API",
    version = __version__
    
)
app.add_middleware(
    CORSMiddleware,
    allow_origins = ["http://localhost:8080"],
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"]
)


#import router



#return version

class Version(BaseModel):
    title : str = app.title,
    version : str = __version__

    
@app.get(
    "/",
    description = "Return API Version",
    response_model = Version
)
async def version():
    return Version()

