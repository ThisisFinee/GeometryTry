import math
from typing import Dict, Any, Optional
from pydantic import BaseModel, Field

from app.shapes.base import Shape
from app.shapes.base import register_shape


class CircleModel(BaseModel):
    radius: float = Field(..., gt=0, description="Radius must be positive")

@register_shape("circle")
class Circle(Shape):
    def __init__(self, radius: float):
        self.radius = radius

    def area(self) -> float:
        return math.pi * self.radius ** 2

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "Circle":
        model = CircleModel(**data)
        return cls(radius=model.radius)
    
    def specific_shape_check(self) -> Optional[Dict[str, Any]]:
        return {"text": "Valid circle", "is_specific": False}
    
    def _is_specific(self):
        return True