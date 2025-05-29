from typing import Optional, Dict, Any
from fastapi import HTTPException
from app.shapes.base import shape_registry, Shape

class ShapeFactory:
    def list_shapes(self) -> Dict[str, str]:
        return {name: cls.__name__ for name, cls in shape_registry.items()}

    def create(self, shape_type: Optional[str], params: Dict[str, Any]) -> Shape:
        errors = []
        if shape_type:
            cls = shape_registry.get(shape_type)
            if not cls:
                raise HTTPException(status_code=400, detail=f"Unknown shape type '{shape_type}'")
            try:
                shape = cls.from_dict(params)
            except Exception as e:
                raise HTTPException(status_code=400, detail=f"Invalid parameters for {shape_type}: {e}")
            return shape
        
        if not params:
            raise HTTPException(status_code=400, detail=f"The parameters are empty")
        
        for name, cls in shape_registry.items():
            try:
                candidate = cls.from_dict(params)
                return candidate
            except Exception as e:
                errors.append(f"{name}: {e}")

        detail = "Cannot detect shape type. Tried: " + ", ".join(errors)
        raise HTTPException(status_code=400, detail=detail)