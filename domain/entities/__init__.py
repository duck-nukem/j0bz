from typing import Dict, Any


class Entity:
    readonly_field_names = []

    def update(self, updates: Dict[str, Any]) -> None:
        for key, value in updates.items():
            if key in self.readonly_field_names:
                continue
            setattr(self, key, value)