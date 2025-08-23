# --- EJERCICIO 1: ProductCatalog (Gestión de inventario) ---
class ProductCatalog:
    def __init__(self):
        self.products = {}  # {id: {"name": str, "price": float}}

    def add_product(self, product_id: int, name: str, price: float):

    def remove_product(self, product_id: int):


    def get_average_price(self) -> float:
      

# --- EJERCICIO 2: OrderManager ---
class OrderManager:
    def __init__(self):
        self.__orders = []

    def place_order(self, order_id: int, amount: float):

    def cancel_order(self, order_id: int):

    def get_total_revenue(self) -> float:


# --- EJERCICIO 3: EventBus (Observer) ---
class EventBus:
    def __init__(self):
        self.listeners = []

    def subscribe(self, func):

    def publish(self, event: str):



# --- EJERCICIO 4: Configuration (Singleton) ---
class Configuration:
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__instance.settings = {}
        return cls.__instance

    def set_setting(self, key: str, value):

    def get_setting(self, key: str):
