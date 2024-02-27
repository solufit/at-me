"""Module providing a function printing python version."""

import os
from datetime import datetime, date
from pydantic import BaseModel, Field
from typing import List
from motor.motor_asyncio import AsyncIOMotorClient

client = AsyncIOMotorClient(
    f"mongodb://{os.getenv('MONGO_INITDB_ROOT_USERNAME')}:{os.getenv('MONGO_INITDB_ROOT_PASSWORD')}@{os.getenv('MONGO_HOST')}:27017/{os.getenv('MONGO_INITDB_DATABASE')}?authSource=admin&retryWrites=true&w=majority"
)
db = client.get_database(os.getenv("MONGO_INITDB_DATABASE"))
user_collection = db.get_collection("user")
class ProviderInfo(BaseModel):
    id: str = Field(...)
    photoURL: str = Field(...)
    displayName: str = Field(...)
    email: str = Field(...)
    linkcoede: str = Field(...)

class Providers(BaseModel):
    atme: ProviderInfo = Field(...)
    google: ProviderInfo= Field(...)
    github: ProviderInfo = Field(...)

class User(BaseModel):
    """_summary_

    Args:
        BaseModel (_type_): _description_
    """
    userId: str = Field(...)
    username: str = Field(...)
    email: str = Field(...)
    photoURL: str = Field(...)
    calenderProvider: str = Field(...)
    taskProvider: str = Field(...)
    providers: Providers = Field(...)
    created_at: datetime = Field(...)


    