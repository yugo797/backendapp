from sqlalchemy.orm import Session
from models.movie import Category
from schemas.category import CategoryCreate


def get_category(db: Session, category_id: int):
    return db.query(Category).filter(Category.id == category_id).first()


def create_category(db: Session, category: CategoryCreate):
    db_category = Category(**category.dict())
    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    return db_category

# from sqlalchemy.ext.asyncio import AsyncSession
# from sqlalchemy.future import select
# from sqlalchemy.orm import selectinload

# async def get_category(db: AsyncSession, category_id: int):
#     try:
#         result = await db.execute(select(Category).filter(Category.id == category_id))
#         return result.scalars().first()
#     except Exception as e:
#         print(f"Error getting category: {e}")
#         raise
#     finally:
#         await db.close()

# async def create_category(db: AsyncSession, category: CategoryCreate):
#     db_category = Category(**category.dict())
#     try:
#         db.add(db_category)
#         await db.commit()
#         await db.refresh(db_category)
#         return db_category
#     except Exception as e:
#         await db.rollback()
#         print(f"Error creating category: {e}")
#         raise
#     finally:
#         await db.close()
