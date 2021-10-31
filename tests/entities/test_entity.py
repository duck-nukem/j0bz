import unittest
from dataclasses import dataclass
from uuid import uuid4

from domain.entities import Entity


@dataclass
class _DerivedEntity(Entity):
    readonly_field_names = ['id']

    id = uuid4()
    name: str


class TestEntity(unittest.TestCase):
    def test_update(self):
        entity = _DerivedEntity(name='A')

        entity.update({'name': 'B'})

        self.assertEqual(entity.name, 'B')

    def test_update_with_readonly_field(self):
        entity = _DerivedEntity(name='A')
        original_id = entity.id

        entity.update({'id': uuid4()})

        self.assertEqual(entity.id, original_id)


if __name__ == '__main__':
    unittest.main()
