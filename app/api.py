from fastapi import APIRouter, HTTPException
from typing import Dict, Any
from app.models import ShapeRequest, ShapeAreaResponse
from app.factory import ShapeFactory

router = APIRouter()
factory = ShapeFactory()

@router.post("/compute-area", response_model=ShapeAreaResponse)
def compute_area(request: ShapeRequest):
    try:
        shape = factory.create(request.type, request.parameters)
    except HTTPException as e:
        raise e

    area = shape.area()
    additional = shape.specific_shape_check()
    return ShapeAreaResponse(
        type=shape.__class__.__name__,
        area=area,
        additional=additional
    )

@router.get("/shapes", response_model=Dict[str, str])
def list_shapes():
    return factory.list_shapes()