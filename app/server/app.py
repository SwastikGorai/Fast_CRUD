from fastapi import FastAPI
from server.database import init_db
from server.routes.prod_rev import router as Router


app = FastAPI()
app.include_router(Router, tags=["Product Reviews"], prefix="/reviews")


@app.on_event("startup")
async def start_db():
    await init_db()

@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to this fantastic app!"}




