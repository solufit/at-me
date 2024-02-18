from pydantic import BaseModel, Field
from datetime import datetime, timedelta
import motor
from motor.motor_asyncio import AsyncIOMotorClient
from typing import Optional
import os

# MongoDBの設定
client = motor.motor_asyncio.AsyncIOMotorClient(f"mongodb://{os.getenv('MONGO_INITDB_ROOT_USERNAME')}:{os.getenv('MONGO_INITDB_ROOT_PASSWORD')}@{os.getenv('MONGO_HOST')}:27017/{os.getenv('MONGO_INITDB_DATABASE')}?authSource=admin&retryWrites=true&w=majority")
db = client.get_database(os.getenv('MONGO_INITDB_DATABASE'))
user_setting_collection = db.get_collection("user_setting")

# Pydanticモデルを定義
class Earthquake(BaseModel):
    id: str = Field(alias="_id", default=None)
    Theme: str = Field(...)
    Worktime: list = Field(...)