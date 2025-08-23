class InventoryManager:
    def __init__(self):
        self.items = {}

    def add_item(self, name: str, quantity: int):
        if name in self.items:
            self.items[name] += quantity
        else:
            self.items[name] = quantity

    def remove_item(self, name: str, quantity: int):
        if name in self.items:
            self.items[name] -= quantity
            if self.items[name] <= 0:
                del self.items[name]

    def get_quantity(self, name: str) -> int:
        return self.items.get(name, 0)

    def total_items(self) -> int:
        return len(self.items)
