# --- EJERCICIO 1: ProductCatalog (Gestión de inventario) ---
class ProductCatalog:
    def __init__(self):
        self.products = {}  # {id: {"name": str, "price": float}}

    def add_product(self, product_id: int, name: str, price: float):
        self.products[product_id] = {"name": name, "price": price}

    def remove_product(self, product_id: int):
        if product_id in self.products:
            del self.products[product_id]

    def get_average_price(self) -> float:
        if not self.products:
            return 0
        return sum(p["price"] for p in self.products.values()) / len(self.products)


# --- EJERCICIO 2: OrderManager ---
class OrderManager:
    def __init__(self):
        self.__orders = []

    def place_order(self, order_id: int, amount: float):
        self.__orders.append({"order_id": order_id, "amount": amount})

    def cancel_order(self, order_id: int):
        self.__orders = [o for o in self.__orders if o["order_id"] != order_id]

    def get_total_revenue(self) -> float:
        return sum(o["amount"] for o in self.__orders)


# --- EJERCICIO 3: EventBus (Observer) ---
class EventBus:
    def __init__(self):
        self.listeners = []

    def subscribe(self, func):
        self.listeners.append(func)

    def publish(self, event: str):
        for listener in self.listeners:
            listener(event)


# --- EJERCICIO 4: Configuration (Singleton) ---
class Configuration:
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__instance.settings = {}
        return cls.__instance

    def set_setting(self, key: str, value):
        self.settings[key] = value

    def get_setting(self, key: str):
        return self.settings.get(key)
