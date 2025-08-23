# =========================
# EJERCICIO 1: ProductInventory
# =========================
# Implementa una clase que gestione un inventario de productos. Cada producto tiene
# nombre, cantidad y precio unitario. La clase debe permitir:
# - agregar productos,
# - eliminar productos,
# - calcular valor total del inventario,
# - obtener el producto más caro.

class ProductInventory:
    def __init__(self):
        """Inicializa inventario vacío"""
        self.products = []  # lista de diccionarios: {"name": str, "qty": int, "price": float}

    def add_product(self, name: str, qty: int, price: float):
        """Agrega producto nuevo o actualiza cantidad y precio si existe"""
        for prod in self.products:
            if prod["name"] == name:
                prod["qty"] += qty
                prod["price"] = price
                return
        self.products.append({"name": name, "qty": qty, "price": price})

    def remove_product(self, name: str):
        """Elimina producto por nombre"""
        for prod in self.products:
            if prod["name"] == name:
                self.products.remove(prod)
                break

    def get_total_value(self) -> float:
        """Devuelve el valor total del inventario"""
        total = 0
        for prod in self.products:
            total += prod["qty"] * prod["price"]
        return total

    def get_most_expensive(self) -> dict:
        """Devuelve el producto con precio unitario más alto"""
        if not self.products:
            return None
        max_price = 0
        max_prod = None
        for prod in self.products:
            if prod["price"] > max_price:
                max_price = prod["price"]
                max_prod = prod
        return max_prod


# =========================
# EJERCICIO 2: OrderQueue
# =========================
# Implementa una clase que maneje pedidos en una cola FIFO. Cada pedido tiene un
# ID y prioridad. Métodos:
# - agregar pedido
# - procesar siguiente pedido (eliminarlo de la cola)
# - obtener lista de pedidos pendientes ordenados por prioridad

class OrderQueue:
    def __init__(self):
        """Inicializa lista de pedidos vacía"""
        self.orders = []  # lista de diccionarios: {"id": str, "priority": int}

    def add_order(self, id: str, priority: int):
        self.orders.append({"id": id, "priority": priority})

    def process_next(self) -> str:
        """Devuelve el pedido de mayor prioridad y lo elimina"""
        if not self.orders:
            return None
        max_priority = -1
        next_order = None
        for order in self.orders:
            if order["priority"] > max_priority:
                max_priority = order["priority"]
                next_order = order
        self.orders.remove(next_order)
        return next_order["id"]

    def get_pending_orders(self) -> list:
        """Devuelve pedidos ordenados por prioridad descendente"""
        sorted_orders = []
        temp_orders = self.orders.copy()
        while temp_orders:
            max_priority = -1
            next_order = None
            for order in temp_orders:
                if order["priority"] > max_priority:
                    max_priority = order["priority"]
                    next_order = order
            sorted_orders.append(next_order["id"])
            temp_orders.remove(next_order)
        return sorted_orders


# =========================
# EJERCICIO 3: TemperatureMonitor (Observer Pattern)
# =========================
# Implementa un sistema de monitoreo de temperatura que:
# - agrega lecturas
# - permite suscribirse a alertas cuando se supera un umbral
# - devuelve temperatura máxima registrada

class TemperatureMonitor:
    def __init__(self, threshold: float):
        self.temps = []
        self.threshold = threshold
        self.subscribers = []

    def add_temperature(self, value: float):
        self.temps.append(value)
        if value > self.threshold:
            self.notify_alert(value)

    def subscribe(self, func):
        if func not in self.subscribers:
            self.subscribers.append(func)

    def notify_alert(self, value: float):
        for func in self.subscribers:
            func(value)

    def get_max_temperature(self) -> float:
        if not self.temps:
            return None
        max_temp = self.temps[0]
        for t in self.temps:
            if t > max_temp:
                max_temp = t
        return max_temp


# =========================
# TESTS DEL SIMULACRO
# =========================

def test_product_inventory():
    inv = ProductInventory()
    inv.add_product("Laptop", 10, 1500)
    inv.add_product("Monitor", 5, 300)
    inv.add_product("Laptop", 5, 1600)  # actualización de cantidad y precio

    assert inv.get_total_value() == (15*1600 + 5*300)
    assert inv.get_most_expensive()["name"] == "Laptop"

    inv.remove_product("Monitor")
    assert len(inv.products) == 1
    print("ProductInventory tests passed ✅")

def test_order_queue():
    queue = OrderQueue()
    queue.add_order("A001", 2)
    queue.add_order("A002", 5)
    queue.add_order("A003", 3)

    assert queue.process_next() == "A002"
    assert queue.get_pending_orders() == ["A003", "A001"]
    print("OrderQueue tests passed ✅")

def test_temperature_monitor():
    alerts = []

    def alert_func(value):
        alerts.append(value)

    monitor = TemperatureMonitor(threshold=30)
    monitor.subscribe(alert_func)

    monitor.add_temperature(25)
    assert monitor.get_max_temperature() == 25
    assert alerts == []

    monitor.add_temperature(35)
    assert monitor.get_max_temperature() == 35
    assert alerts == [35]
    print("TemperatureMonitor tests passed ✅")


# =========================
# EJECUCIÓN DE TESTS
# =========================

if __name__ == "__main__":
    print("----- Simulacro ICA #6 -----\n")
    test_product_inventory()
    test_order_queue()
    test_temperature_monitor()
    print("\nTodos los tests completados ✅ ¡Simulacro listo!")
