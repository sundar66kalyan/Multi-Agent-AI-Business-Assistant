from pydantic import BaseModel
from typing import Any
from typing import Optional


class AgentResponse(BaseModel):

    agent: str

    success: bool = True

    message: str

    data: Optional[Any] = None