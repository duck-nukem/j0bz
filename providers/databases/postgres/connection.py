from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def get_engine_url():
    import os
    return "postgresql+psycopg2://%s:%s@%s/%s" % (
        os.getenv("DB_USER", "postgres"),
        os.getenv("DB_PASSWORD", "password"),
        os.getenv("DB_HOST", "db"),
        os.getenv("DB_NAME", "postgres"),
    )


ENGINE_URL = get_engine_url()
db_engine = create_engine(
    ENGINE_URL,
    echo=True,
    future=True,
)

connect = sessionmaker(
    db_engine,
    expire_on_commit=False,
)
