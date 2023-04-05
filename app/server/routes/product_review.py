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
    if not review:
        raise HTTPException(
            status_code=404,
            detail=f'No review record found for id {id}'
        )
    return review

@router.get('/', response_description='all review records retrieved')
async def get_all_reviews() -> List[ProductReview]:
    reviews = await ProductReview.find_all().to_list()
    return reviews

@router.put('/{id}', response_description='review record pertaining to ID updated')
async def update_student_data(id: PydanticObjectId, req: UpdateProductReview) -> ProductReview:
    req = {k : v for k,v in req.dict().items() if v is not None}
    update_query = {"$set": {
        field: value for field, value in req.items()
    }}
    review = await ProductReview.get(id)
    if not review:
        raise HTTPException(
            status_code=404,
            detail=f'No review record found for id {id}'
        )
    await review.update(update_query)
    return review

@router.delete("/{id}", response_description='review record pertaining to ID deleted')
async def delete_review(id: PydanticObjectId) -> dict:
    record = await ProductReview.get(id)

    if not record:
        raise HTTPException(
            status_code=404,
            detail=f'No review record found for id {id}'
        )
    
    await record.delete()
    return {
        'message': 'Record deleted successfully'
    }