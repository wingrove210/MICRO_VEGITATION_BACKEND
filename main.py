from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers.product_router import product_router
from database import Base, engine
# Создание таблиц в базе данных
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Настройка CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Подключение маршрутов
app.include_router(product_router, prefix="/product", tags=["Products"])

