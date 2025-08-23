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
        current = self.items.get(name,0)
        self.items[name] = min(current + quantity, self.max_per_item)

    def remove_item(self, name: str, quantity: int):
        """Elimina cierta cantidad de producto del inventario. Si queda 0 o menos, eliminarlo."""
        if name in self.items:
            self.items[name] -= quantity
            if self.items[name] <= 0:
                del self.items[name]

    def get_quantity(self, name: str) -> int:
        """Devuelve la cantidad actual de un producto, o 0 si no existe."""
        return self.items.get(name,0)

    def total_inventory(self) -> int:
        """Devuelve la suma de todos los productos en inventario."""
        return sum(self.items.values())


# --- EJERCICIO 2: ProductionLine ---
class ProductionLine:
    def __init__(self):
        """Inicializa la línea de producción vacía."""
        self.production_log = []  # lista de cantidades producidas por día

    def produce(self, quantity: int):
        """Agrega una cantidad producida en un día."""
        self.production_log.append(quantity)

    def total_production(self) -> int:
        """Devuelve la producción total."""
        produccion = 0
        for i in range(len(self.production_log)):
            produccion += self.production_log[i]
        return produccion

    def average_production(self) -> float:
        """Devuelve la producción promedio por día, o None si no hay datos."""
        if self.production_log == []:
            return None
        else:
            produccion = 0
            for i in range(len(self.production_log)):
                produccion += self.production_log[i]
            return produccion/(len(self.production_log))

    def max_production(self) -> int:
        """Devuelve la producción máxima registrada, o None si no hay datos."""
        if self.production_log == []:
            return None
        return max(self.production_log)

    def reset_production(self, all_days: bool = True):
        """Resetea la producción. Si all_days=False, resetea solo el último día."""
        if all_days:
            self.production_log.clear()
        else:
            if self.production_log:
                self.production_log.pop()            


# --- EJERCICIO 3: TemperatureMonitor ---
class TemperatureMonitor:
    def __init__(self, alert_threshold: float):
        """Inicializa monitor con umbral de alerta."""
        self.temperatures = []
        self.alert_threshold = alert_threshold

    def add_temperature(self, temp: float):
        """Agrega una temperatura al registro."""
        self.temperatures.append(temp)

    def get_median(self) -> float:
        """Devuelve la mediana actual, o None si no hay datos."""
        if self.temperatures == []:
            return None
        else:
            sorted_temp = sorted(self.temperatures)
            mid = len(sorted_temp)//2
            if mid % 2 == 0:
                return (sorted_temp[mid-1]+sorted_temp[mid])/2
            else:
                return sorted_temp[mid]                    

    def alert(self) -> bool:
        """Devuelve True si la última temperatura supera el umbral."""
        return self.temperatures[-1] > self.alert_threshold


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
