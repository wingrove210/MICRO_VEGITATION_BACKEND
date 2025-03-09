import os
from fastapi import APIRouter, Depends, File, Form, HTTPException, UploadFile
from sqlalchemy import insert, select, delete
from sqlalchemy.ext.asyncio import AsyncSession
from database import get_async_session
from models.product import Product
from services.files import get_url

product_router = APIRouter()

@product_router.post("/products")
async def create_product(
    name: str = Form(...),
    description: str = Form(...),
    image: UploadFile = File(...),
    price: int = Form(...),
    is_avalible: bool = Form(...),
    stock: int = Form(...),
    db: AsyncSession = Depends(get_async_session)
):
   url_image = await get_url([image]) 
   
   new_product = Product(
       name=name,
       description=description,
       image=url_image[0],
       price=price,
       is_avalible=is_avalible,
       stock=stock 
   )
   query = insert(Product).values(
       name=name,
       description=description,
       image=url_image[0],
       price=price,
       is_avalible=is_avalible,
       stock=stock
   )
   await db.execute(query)
   await db.commit()
   return new_product

@product_router.get('/products')
async def get_products(db: AsyncSession = Depends(get_async_session)):
    query = select(Product)
    data = await db.execute(query)
    datas = data.mappings.all()
    products = []
    for row in datas:
        products.append(row["Track"])
    return products

@product_router.get('/products/{product_id}')
async def get_product(product_id: int, db: AsyncSession = Depends(get_async_session)):
    query = select(Product).where(Product.id == product_id)
    result = await db.execute(query)
    product = result.scalar_one_or_none()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    
@product_router.delete('/products/{product_id}')
async def delete_product(product_id: int, db: AsyncSession = Depends(get_async_session)):
    query = select(Product).where(Product.id == product_id)
    result = await db.execute(query)
    product = result.scalar_one_or_none()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    
    stmt = delete(Product).where(Product.id == product_id)
    await db.execute(stmt)
    await db.commit()
    return product
   