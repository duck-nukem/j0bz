from typing import Callable, Dict

from sqlalchemy import insert, select, update

from providers.databases.postgres.connection import connect


class GenericDAO:
    def __init__(self, db_model_class: Callable) -> None:
        self.db_model_class = db_model_class
        super().__init__()

    def create(self, values: Dict) -> int:
        with connect() as db:
            statement = insert(self.db_model_class).values(values)
            result = db.execute(statement)
            db.commit()

            return result.inserted_primary_key[0]

    def get_one(self, **kwargs):
        with connect() as db:
            query = select(self.db_model_class).filter_by(**kwargs)
            results = db.execute(query)
            (result,) = results.one()

            return result

    def get_all(self, page_size: int = 10, page_number: int = 1):
        with connect() as db:
            query = select(self.db_model_class) \
                .limit(page_size) \
                .offset((page_number - 1) * page_size)
            results = db.execute(query).fetchall()

            # Arrived here via debugging the entries inside results, must be a better way
            return [r._data[0] for r in results]

    def update(self, primary_key: int, values: Dict):
        with connect() as db:
            statement = update(self.db_model_class) \
                .where(self.db_model_class.id == primary_key) \
                .values(**values)
            db.execute(statement)
            db.commit()
