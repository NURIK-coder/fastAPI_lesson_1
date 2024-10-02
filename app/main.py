from fastapi import FastAPI

app = FastAPI()

from app.main_app.router import router as main_router

app.include_router(main_router)
