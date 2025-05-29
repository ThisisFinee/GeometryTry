from abc import ABC, abstractmethod
from typing import Dict, Type, Any, Optional

from pydantic import BaseModel, Field, field_validator


class Shape(ABC):
    @abstractmethod
    def area(self) -> float:
        """Compute the area of the shape"""
        pass

    def _is_specific(self) -> bool:
        pass

    @abstractmethod
    def specific_shape_check(self) -> Dict[str, Any]:
        """Perform shape-specific check"""
        pass

    @classmethod
    @abstractmethod
    def from_dict(cls, data: Dict[str, Any]) -> "Shape":
        """Create shape instance from dict"""
        pass

shape_registry: Dict[str, Type[Shape]] = {}

def register_shape(name: str):
    def decorator(cls: Type[Shape]):
        shape_registry[name] = cls
        return cls
    return decorator