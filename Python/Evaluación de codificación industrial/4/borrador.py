# =========================
# Simulacro CodeSignal ICA
# =========================

# --- EJERCICIO 1: InventoryManager ---
class InventoryManager:
    def __init__(self, max_per_item: int):
        """Inicializa un inventario vacío con límite máximo por producto."""
        self.items = {}
        self.max_per_item = max_per_item

    def add_item(self, name: str, quantity: int):
        """Agrega una cantidad de producto al inventario. No superar max_per_item."""
        pass

    def remove_item(self, name: str, quantity: int):
        """Elimina cierta cantidad de producto del inventario. Si queda 0 o menos, eliminarlo."""
        pass

    def get_quantity(self, name: str) -> int:
        """Devuelve la cantidad actual de un producto, o 0 si no existe."""
        pass

    def total_inventory(self) -> int:
        """Devuelve la suma de todos los productos en inventario."""
        pass


# --- EJERCICIO 2: ProductionLine ---
class ProductionLine:
    def __init__(self):
        """Inicializa la línea de producción vacía."""
        self.production_log = []  # lista de cantidades producidas por día

    def produce(self, quantity: int):
        """Agrega una cantidad producida en un día."""
        pass

    def total_production(self) -> int:
        """Devuelve la producción total."""
        pass

    def average_production(self) -> float:
        """Devuelve la producción promedio por día, o None si no hay datos."""
        pass

    def max_production(self) -> int:
        """Devuelve la producción máxima registrada, o None si no hay datos."""
        pass

    def reset_production(self, all_days: bool = True):
        """Resetea la producción. Si all_days=False, resetea solo el último día."""
        pass


# --- EJERCICIO 3: TemperatureMonitor ---
class TemperatureMonitor:
    def __init__(self, alert_threshold: float):
        """Inicializa monitor con umbral de alerta."""
        self.temperatures = []
        self.alert_threshold = alert_threshold

    def add_temperature(self, temp: float):
        """Agrega una temperatura al registro."""
        pass

    def get_median(self) -> float:
        """Devuelve la mediana actual, o None si no hay datos."""
        pass

    def alert(self) -> bool:
        """Devuelve True si la última temperatura supera el umbral."""
        pass


# =========================
# TESTS DEL SIMULACRO
# =========================

def test_inventory_manager():
    inv = InventoryManager(max_per_item=10)
    inv.add_item("apple", 5)
    inv.add_item("apple", 10)  # no debe superar 10
    inv.add_item("banana", 3)

    assert inv.get_quantity("apple") == 10
    assert inv.get_quantity("banana") == 3

    inv.remove_item("apple", 4)
    assert inv.get_quantity("apple") == 6

    inv.remove_item("banana", 5)
    assert inv.get_quantity("banana") == 0

    assert inv.total_inventory() == 6
    print("InventoryManager tests passed ✅")


def test_production_line():
    line = ProductionLine()
    line.produce(10)
    line.produce(20)
    line.produce(15)

    assert line.total_production() == 45
    assert line.average_production() == 15
    assert line.max_production() == 20

    line.reset_production(all_days=False)
    assert line.total_production() == 30

    line.reset_production()
    assert line.total_production() == 0
    print("ProductionLine tests passed ✅")


def test_temperature_monitor():
    monitor = TemperatureMonitor(alert_threshold=30.0)
    monitor.add_temperature(25)
    monitor.add_temperature(28)
    monitor.add_temperature(32)

    assert monitor.get_median() == 28
    assert monitor.alert() == True

    monitor.add_temperature(27)
    assert monitor.get_median() == 27.5
    assert monitor.alert() == False
    print("TemperatureMonitor tests passed ✅")


# =========================
# EJECUCIÓN DE TESTS
# =========================

if __name__ == "__main__":
    print("----- Simulacro ICA -----")
    print("Tiempo sugerido: 90 minutos")
    print("Completa las clases antes de correr los tests.\n")
    
    test_inventory_manager()
    test_production_line()
    test_temperature_monitor()
    
    print("\nTodos los tests completados ✅")
