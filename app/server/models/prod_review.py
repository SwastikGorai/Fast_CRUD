from datetime import datetime
from beanie import Document
from pydantic import BaseModel, Field
from typing import Optional, List


class ProdReview(Document):
    name: str
    product: str
    review: str
    rating: float
    date: datetime = datetime.now()
    
    class Settings:
        name = "wew"
        
    
    class Config:
        schema_extra = {
            "example": {
                "name": "John Doe",
                "review": "This is a review",
                "rating": 4.2,
                "date": datetime.now()
            }
        }   
        
    
    
    
    
class UpdateReview(BaseModel):
    name : Optional[str]
    product : Optional[str]
    review : Optional[str]
    rating : Optional[float]
    date : Optional[datetime]
    
    class Config:
        schema_extra = {
            "example": {
                "name": "John Doe",
                "review": "This is a review",
                "rating": 4.2,
                "date": datetime.now()
            }
        }
    