from pydantic import BaseModel, Field

from typing import Optional, List



class Result(BaseModel):
    success : bool = Field(True, description="Result of tasks")