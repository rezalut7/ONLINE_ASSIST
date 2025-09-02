from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import declarative_base
from .config import settings

Base = declarative_base()
engine = create_async_engine(settings.DATABASE_URL, echo=False, future=True)
async_session = async_sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)

async def init_db() -> None:
    from . import models  # noqa: F401 ensure models are imported
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
