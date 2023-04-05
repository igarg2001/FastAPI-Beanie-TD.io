from beanie import PydanticObjectId
from fastapi import APIRouter, HTTPException
from typing import List

from app.server.models.product_review import ProductReview, UpdateProductReview

router = APIRouter()

@router.post('/', response_description='review added to db')
async def add_product_review(review: ProductReview) -> dict:
    await review.create()
    return {'message': 'Review added successfully'}

@router.get('/{id}', response_description='review record corresponding to ID retrieved')
async def get_review_by_id(id: PydanticObjectId) -> ProductReview:
    review = await ProductReview.get(id)
    return review

@router.get('/', response_description='all review records retrieved')
async def get_all_reviews() -> List[ProductReview]:
    reviews = await ProductReview.find_all().to_list()
    return reviews