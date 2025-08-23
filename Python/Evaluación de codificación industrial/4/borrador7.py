# =========================
# Simulacro ICA #6 – Borrador
# =========================
# Tiempo sugerido: 90 minutos
# Objetivo: Evaluar habilidades de codificación industrial.
# 4 ejercicios con clases, manejo de listas de diccionarios y patrones básicos.

# =========================
# EJERCICIO 1: ProductInventory
# =========================
# Gestiona inventario de productos:
# - Agregar producto (actualiza si ya existe)
# - Eliminar producto
# - Calcular valor total
# - Obtener producto más caro

class ProductInventory:
    def __init__(self):
        """Inicializa lista vacía de productos."""
        self.products = []  # cada producto: {"name": str, "qty": int, "price": float}

    def add_product(self, name: str, qty: int, price: float):
        """Agrega o actualiza un producto."""
        pass  # implementar

    def remove_product(self, name: str):
        """Elimina un producto por nombre si existe."""
        pass  # implementar

    def total_value(self) -> float:
        """Calcula el valor total del inventario."""
        pass  # implementar

    def most_expensive(self) -> dict:
        """Devuelve el producto más caro por precio unitario."""
        pass  # implementar


# =========================
# EJERCICIO 2: OrderManager
# =========================
# Gestiona pedidos:
# - Agregar pedido con id y total
# - Cancelar pedido
# - Obtener pedido con mayor total
# - Calcular suma de todos los pedidos

class OrderManager:
    def __init__(self):
        """Inicializa lista vacía de pedidos."""
        self.orders = []  # cada pedido: {"id": int, "total": float}

    def add_order(self, order_id: int, total: float):
        """Agrega un pedido."""
        pass  # implementar

    def cancel_order(self, order_id: int):
        """Elimina un pedido por id si existe."""
        pass  # implementar

    def highest_order(self) -> dict:
        """Devuelve el pedido con mayor total."""
        pass  # implementar

    def total_orders(self) -> float:
        """Suma de todos los pedidos."""
        pass  # implementar


# =========================
# EJERCICIO 3: TaskManager
# =========================
# Gestiona tareas:
# - Agregar tarea con prioridad
# - Obtener siguiente tarea (más alta prioridad)
# - Listar todas las tareas ordenadas por prioridad descendente

class TaskManager:
    def __init__(self):
        """Inicializa lista vacía de tareas."""
        self.tasks = []  # cada tarea: {"task": str, "priority": int}

    def add_task(self, task: str, priority: int):
        """Agrega una tarea con prioridad."""
        pass  # implementar

    def get_next_task(self) -> str:
        """Devuelve la tarea más prioritaria y la elimina de la lista."""
        pass  # implementar

    def get_all_tasks(self) -> list:
        """Devuelve todas las tareas ordenadas por prioridad descendente."""
        pass  # implementar


# =========================
# EJERCICIO 4: SensorNetwork
# =========================
# Sistema de sensores:
# - Agregar sensor con valor
# - Suscribir alertas
# - Notificar cuando un sensor supera umbral
# - Obtener valor máximo registrado

class SensorNetwork:
    def __init__(self, threshold: float):
        self.sensors = []  # valores de sensores
        self.threshold = threshold
        self.subscribers = []  # funciones de alerta

    def add_sensor(self, value: float):
        """Agrega lectura y notifica si supera umbral."""
        pass  # implementar

    def subscribe(self, func):
        """Suscribe función de alerta."""
        pass  # implementar

    def notify_alert(self, value: float):
        """Notifica a todas las funciones suscritas."""
        pass  # implementar

    def get_max_sensor(self) -> float:
        """Devuelve el valor máximo registrado."""
        pass  # implementar


# =========================
# TESTS DEL SIMULACRO
# =========================

def test_product_inventory():
    inv = ProductInventory()
    inv.add_product("Laptop", 5, 1000)
    inv.add_product("Phone", 10, 500)
    # aquí irán asserts para comprobar implementaciones
    print("ProductInventory tests listos ✅")

def test_order_manager():
    om = OrderManager()
    om.add_order(1, 250)
    om.add_order(2, 400)
    # asserts para comprobar
    print("OrderManager tests listos ✅")

def test_task_manager():
    tm = TaskManager()
    tm.add_task("Email client", 3)
    tm.add_task("Write report", 5)
    # asserts
    print("TaskManager tests listos ✅")

def test_sensor_network():
    triggered = []
    def alert_func(value):
        triggered.append(value)
    sn = SensorNetwork(threshold=10)
    sn.subscribe(alert_func)
    sn.add_sensor(12)
    # asserts
    print("SensorNetwork tests listos ✅")


# =========================
# EJECUCIÓN DE TESTS
# =========================
if __name__ == "__main__":
    print("----- Simulacro ICA #6 (Borrador) -----")
    test_product_inventory()
    test_order_manager()
    test_task_manager()
    test_sensor_network()
    print("Todos los tests listos para implementar ✅")
