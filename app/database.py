from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

# from config import settings
from app.config import settings

engine = create_async_engine(settings.DATABASE_URL)

async_session_maker = sessionmaker(engine, Class_=AsyncSession, expire_on_commit=False)

class Base(DeclarativeBase):
    pass