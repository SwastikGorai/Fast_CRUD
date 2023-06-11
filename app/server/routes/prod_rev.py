from beanie import PydanticObjectId
from fastapi import APIRouter, HTTPException
from typing import List

from server.models.prod_review import ProdReview, UpdateReview


router = APIRouter()



@router.post("/", response_description="Review added 👌")
async def add_product_review(review: ProdReview) -> dict:
    await review.create()
    return {"message": "Review added successfully"}
