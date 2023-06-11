from beanie import init_beanie
import motor.motor_asyncio
import os
from server.models.prod_review import ProdReview
from dotenv import load_dotenv

load_dotenv()
uri = os.getenv("MONGODB_URI")
print(uri)

async def init_db():
    client = motor.motor_asyncio.AsyncIOMotorClient(uri)

    await init_beanie(database=client.Prd_Review, document_models=[ProdReview])