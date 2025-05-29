import math
from typing import Dict, Any, Optional
from pydantic import BaseModel, Field, field_validator

from app.shapes.base import Shape
from app.shapes.base import register_shape

class TriangleModel(BaseModel):
    a: float = Field(..., gt=0)
    b: float = Field(..., gt=0)
    c: float = Field(..., gt=0)

    @field_validator("c")
    def validate_triangle(cls, v, info):
        data = info.data
        a = data.get("a"); b = data.get("b")
        if a is None or b is None or a + b <= v or a + v <= b or b + v <= a:
            raise ValueError("Sides do not form a valid triangle")
        return v

@register_shape("triangle")
class Triangle(Shape):
    def __init__(self, a: float, b: float, c: float):
        self.a, self.b, self.c = a, b, c

    def area(self) -> float:
        s = (self.a + self.b + self.c) / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))
    
    def _is_specific(self):
        sides = sorted([self.a, self.b, self.c])
        if math.isclose(sides[0]**2 + sides[1]**2, sides[2]**2):
            return True
        else:
            return False

    def specific_shape_check(self) -> Dict[str, Any]:
        if self._is_specific():
            return {"text": "It's a right-anled triangle", "is_specific": True}
        return {"text": "It's not a right-anled triangle", "is_specific": False}

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "Triangle":
        model = TriangleModel(**data)
        return cls(a=model.a, b=model.b, c=model.c)
