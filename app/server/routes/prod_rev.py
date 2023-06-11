from beanie import PydanticObjectId
from fastapi import APIRouter, HTTPException
from typing import List

from server.models.prod_review import ProdReview, UpdateReview


router = APIRouter()



@router.post("/", response_description="Review added 👌")
async def add_product_review(review: ProdReview) -> dict:
    await review.create()
    return {"message": "Review added successfully"}


@router.get("/{id}", response_description="Review record retrieved")
async def get_review_record(id: PydanticObjectId) -> ProdReview:
    review = await ProdReview.get(id)
    return review


@router.get("/", response_description="Review records retrieved")
async def get_reviews() -> List[ProdReview]:
    reviews = await ProdReview.find_all().to_list()
    return reviews



@router.put("/{id}", response_description="Review record updated")
async def update_data(id: PydanticObjectId, request: UpdateReview):
    req = {key: value for key, value in request.dict().items() if value is not None}
    update_query = { 
                    "$set": req
                }
        
    review = await ProdReview.get(id)
    if not review:
        raise HTTPException(
            status_code=404,
            detail="Record not found"
        )

    await review.update(update_query)
    return review




@router.delete("/{id}", response_description="Record deleted")
async def delete_student_data(id: PydanticObjectId) -> dict:
    record = await ProdReview.get(id)

    if not record:
        raise HTTPException(
            status_code=404,
            detail="Record not found!"
        )

    await record.delete()
    return {
        "message": "Record deleted successfully"
    }