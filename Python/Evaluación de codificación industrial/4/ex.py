from in_memory_db import InMemoryDB

class InMemoryDBImpl(InMemoryDB):
    def __init__(self):
        # Estado actual: { key: { field: value } }
        self.db: dict[str, dict[str, int]] = {}

    def set(self, timestamp: int, key: str, field: str, value: int) -> None:
        if key not in self.db:
            self.db[key] = {}
        self.db[key][field] = value

    def get(self, timestamp: int, key: str, field: str) -> int | None:
        return self.db.get(key, {}).get(field, None)

    def compare_and_set(self, timestamp: int, key: str, field: str,
                        expected_value: int, new_value: int) -> bool:
        if key in self.db and field in self.db[key] and self.db[key][field] == expected_value:
            self.db[key][field] = new_value
            return True
        return False

    def compare_and_delete(self, timestamp: int, key: str, field: str,
                           expected_value: int) -> bool:
        if key in self.db and field in self.db[key] and self.db[key][field] == expected_value:
            del self.db[key][field]
            if not self.db[key]:
                del self.db[key]   # opcional: limpiar registros vacíos
            return True
        return False
