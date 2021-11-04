from abc import ABC, abstractmethod
from typing import Dict, List

from providers.databases import GenericDAO


class Repository(ABC):
    dao: GenericDAO

    def create(self, domain_entity):
        created_id = self.dao.create(self.to_db(domain_entity))
        domain_entity.id = created_id

        return domain_entity

    def get(self, primary_key: int):
        return self.from_db(self.dao.get_one(id=primary_key))

    def list(self) -> List:
        return [self.from_db(entity) for entity in self.dao.get_all()]

    def update(self, domain_entity, updated_data: Dict):
        self.dao.update(domain_entity.id, updated_data)

    @abstractmethod
    def to_db(self, domain_entity):
        pass

    @abstractmethod
    def from_db(self, database_instance):
        pass
