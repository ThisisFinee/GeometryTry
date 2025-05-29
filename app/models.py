from pydantic import BaseModel
from typing import Optional, Dict, Any

class ShapeRequest(BaseModel):
    type: Optional[str] = None
    parameters: Dict[str, Any]

class ShapeAreaResponse(BaseModel):
    type: str
    area: float
    additional: Dict[str, Any]