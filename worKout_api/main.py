from fastapi import FastAPI  # type: ignore
from worKout_api.routers import api_router

app = FastAPI(title='worKoutApi')
app.include_router(api_router)
