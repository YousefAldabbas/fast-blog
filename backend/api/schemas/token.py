from datetime import datetime

from typing import List, Union, Optional
from pydantic import BaseModel, root_validator


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    sub: Optional[int] = None
    scope: Optional[str] = None
