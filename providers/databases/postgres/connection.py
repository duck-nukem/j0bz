from sqlalchemy import engine_from_config, pool
from sqlalchemy.ext.asyncio import AsyncEngine, AsyncSession
from sqlalchemy.orm import sessionmaker


def get_engine_url():
    import os
    return "postgresql+asyncpg://%s:%s@%s/%s" % (
        os.getenv("DB_USER", "postgres"),
        os.getenv("DB_PASSWORD", "password"),
        os.getenv("DB_HOST", "db"),
        os.getenv("DB_NAME", "postgres"),
    )


db_engine = AsyncEngine(
    engine_from_config(
        {'sqlalchemy.url': get_engine_url()},
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
        future=True,
    )
)
database = sessionmaker(db_engine, class_=AsyncSession)()
