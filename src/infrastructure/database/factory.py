import logging
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from config import Settings

logger = logging.getLogger(__name__)

def make_connection_string(settings: Settings) -> str:
    # For SQLite, you typically use a file-based database, e.g., "sqlite+aiosqlite:///example.db"
    # Update the connection string to use SQLite
    return f"sqlite+aiosqlite:///{settings.db.name}.db"

def create_pool(url: str) -> sessionmaker:
    # For SQLite with async support, you need to use the aiomysql driver
    engine = create_async_engine(url, echo=False)
    return sessionmaker(
        bind=engine,
        expire_on_commit=False,
        class_=AsyncSession,
        future=True,
        autoflush=False,
    )
