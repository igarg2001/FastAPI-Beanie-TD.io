from beanie import PydanticObjectId
from fastapi import APIRouter, HTTPException
from typing import List

from app.server.models.product_review import ProductReview, UpdateProductReview

router = APIRouter()

@router.post('/', response_description='review added to db')
async def add_product_review(review: ProductReview) -> dict:
    await review.create()
    return {'message': 'Review added successfully'}