# =========================
# EXAMEN DE CODIFICACIÓN INDUSTRIAL – ENTRY/MID LEVEL
# =========================
# Tiempo sugerido: 90 minutos
# Lenguaje: Python 3
# Objetivo: Evaluar habilidades de programación estructurada,
# orientación a objetos, manejo de colecciones y escenarios industriales
# =========================

# -------------------------
# EJERCICIO 1: Inventario de Productos
# -------------------------
# Contexto:
#   Una empresa necesita mantener un inventario de productos.
# Requerimientos:
#   - add_item(code: str, quantity: int): agrega la cantidad especificada del producto.
#       Si el producto ya existe, suma la cantidad.
#   - remove_item(code: str, quantity: int) -> bool: elimina la cantidad especificada
#       si hay suficiente stock, devuelve True; si no, devuelve False.
#   - get_stock(code: str) -> int: retorna el stock actual, 0 si no existe.
#   - get_total_items() -> int: retorna la suma total de todos los productos.

class Inventory:
    def __init__(self):
        # TODO: inicializar estructura interna
        self.inventario = {}

    def add_item(self, code: str, quantity: int):
        if code in self.inventario:
            self.inventario[code] += quantity
        else:
            self.inventario[code] = quantity

    def remove_item(self, code: str, quantity: int) -> bool:
        if code in self.inventario and self.inventario[code] >= quantity:
            self.inventario[code] -=quantity
            if self.inventario[code] == 0:
                del self.inventario[code]
            return True
        return False

    def get_stock(self, code: str) -> int:
        return self.inventario.get(code,0)

    def get_total_items(self) -> int:
        return sum(self.inventario.values())


# -------------------------
# EJERCICIO 2: Registro de Sensores
# -------------------------
# Contexto:
#   Un sistema recibe lecturas de sensores en enteros.
# Requerimientos:
#   - add_reading(value: int): agrega un valor de lectura.
#   - get_median() -> float: retorna la mediana actual.
#       Si el número de lecturas es par, devolver la lectura de la izquierda de las dos centrales.
#   - get_average() -> float: retorna el promedio de las lecturas.
#   - reset(): borra todas las lecturas.

class SensorData:
    def __init__(self):
        self.lecturas = []

    def add_reading(self, value: int):
        self.lecturas.append(value)

    def get_median(self) -> float:

        if not self.lecturas:
            return None

        lecturas_ordenadas = sorted(self.lecturas)
        mitad = len(lecturas_ordenadas) // 2

        if mitad % 2 == 0:
            return lecturas_ordenadas[mitad-1]
        else:
            return lecturas_ordenadas[mitad]

    def get_average(self) -> float:
        if not self.lecturas:
            return None
        
        total = 0
        for t in self.lecturas:
            total +=t
        return total/len(self.lecturas)
        


    def reset(self):
        self.lecturas.clear()


# -------------------------
# EJERCICIO 3: Planificación de Producción
# -------------------------
# Contexto:
#   Se deben organizar órdenes de producción con prioridad.
# Requerimientos:
#   - add_order(order: str, priority: int): agrega una orden con prioridad.
#   - pop_next() -> str: devuelve y elimina la orden con mayor prioridad.
#   - list_orders() -> list: retorna lista de órdenes por prioridad descendente.

class ProductionPlanner:
    def __init__(self):
        self.ordenes = {}

    def add_order(self, order: str, priority: int):
        self.ordenes[order] = priority


    def pop_next(self) -> str:
        if not self.ordenes:
            return None
        
        highest = max(self.ordenes, key=lambda t:self.ordenes[t])
        del self.ordenes[highest]
        return highest

    def list_orders(self) -> list:
        return sorted(self.ordenes.keys(), key=lambda t:self.ordenes[t], reverse=True)
        


# -------------------------
# EJERCICIO 4: Catálogo Versionado
# -------------------------
# Contexto:
#   Cada cambio al catálogo de productos se guarda como versión.
# Requerimientos:
#   - add_product(name: str, price: float)
#   - remove_product(name: str)
#   - update_price(name: str, price: float)
#   - get_version(index: int) -> dict: devuelve snapshot de versión específica
#   - get_latest() -> dict: devuelve snapshot más reciente

class VersionedCatalog:
    def __init__(self):
        self.productos = {}
        self.versiones = []
    
    def snapshot(self):
        self.versiones.append(self.productos.copy())

    def add_product(self, name: str, price: float):
        self.productos[name] = price
        self.snapshot()

    def remove_product(self, name: str):
        if name in self.productos:
            del self.productos[name]
            self.snapshot()

    def update_price(self, name: str, price: float):
        self.productos[name] = price
        self.snapshot()

    def get_version(self, index: int) -> dict:
        if index <= len(self.productos) and index >= 0:
            return self.versiones[index]
        return {}

    def get_latest(self) -> dict:
        if not self.versiones:
            return {}
        return self.versiones[-1]


# =========================
# TESTS DEL EXAMEN
# =========================

def test_inventory():
    inv = Inventory()
    inv.add_item("BOLT", 50)
    inv.add_item("BOLT", 10)
    assert inv.get_stock("BOLT") == 60
    assert inv.remove_item("BOLT", 20) == True
    assert inv.get_stock("BOLT") == 40
    assert inv.remove_item("BOLT", 100) == False
    print("Inventory ✅")


def test_sensor_data():
    sd = SensorData()
    for r in [10, 20, 30, 40]:
        sd.add_reading(r)
    assert sd.get_median() == 20
    assert round(sd.get_average(), 2) == 25
    sd.reset()
    assert sd.get_average() == None
    print("SensorData ✅")


def test_production_planner():
    pp = ProductionPlanner()
    pp.add_order("Order1", 2)
    pp.add_order("Order2", 5)
    pp.add_order("Order3", 3)
    assert pp.pop_next() == "Order2"
    assert pp.list_orders() == ["Order3", "Order1"]
    print("ProductionPlanner ✅")


def test_versioned_catalog():
    vc = VersionedCatalog()
    vc.add_product("Drill", 100)
    vc.add_product("Hammer", 50)
    vc.update_price("Drill", 120)
    vc.remove_product("Hammer")
    assert vc.get_version(0)["Drill"] == 100
    assert vc.get_latest()["Drill"] == 120
    print("VersionedCatalog ✅")


if __name__ == "__main__":
    print("----- Ejecutando Tests del Examen -----")
    test_inventory()
    test_sensor_data()
    test_production_planner()
    test_versioned_catalog()
    print("\nTodos los tests completados ✅ ¡Examen simulado listo!")
