from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers.product_router import product_router
from core.config import settings

app = FastAPI(
    title="Micro Vegitation Bot",
    description="API для бота по микрозелени",
    version="1.0.0",
    docs_url="/api/docs" if settings.ENVIRONMENT == "development" else None,
    redoc_url="/api/redoc" if settings.ENVIRONMENT == "development" else None,
)

origins = [
    "*"
]

@app.on_event("startup")
async def startup_envent():
     pass
 
@app.on_event("shutdown")
async def shutdown_envent():
    pass

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],
    allow_headers=["*"]
)

app.include_router(product_router, prefix='/api')

