# =========================
# EXAMEN DE CODIFICACIÓN INDUSTRIAL – Nivel 4
# =========================
# Tiempo sugerido: 90 minutos
# Lenguaje: Python 3
# Objetivo: Evaluar habilidades de programación estructurada,
# orientación a objetos, manejo de colecciones y casos industriales.
# =========================

# --- EJERCICIO 1: Inventario de Piezas ---
# Contexto:
#   En una planta industrial se debe mantener un inventario digital
#   de piezas de repuesto.
#
# Requerimientos:
#   - add_item(code: str, quantity: int) → agrega una pieza (si ya existe, sumar cantidad)
#   - remove_item(code: str, quantity: int) → quita piezas si hay suficientes (True/False)
#   - get_stock(code: str) → retorna stock de ese código (0 si no existe)
#   - get_total_items() → retorna total de piezas
#
# Ejemplo:
# inv = Inventory()
# inv.add_item("BOLT", 50)
# inv.add_item("BOLT", 10)
# assert inv.get_stock("BOLT") == 60

class Inventory:
    def __init__(self):
        # TODO: inicializar estructuras internas
        self.invetario = {}

    def add_item(self, code: str, quantity: int):
        # TODO: implementar
        
        if code in self.invetario:
            self.invetario[code] += quantity
        else:
            self.invetario[code] = quantity

    def remove_item(self, code: str, quantity: int) -> bool:
        # TODO: implementar
        if code in self.invetario and self.invetario[code] >=quantity:
            self.invetario[code] -= quantity
            if self.invetario[code] == 0:
                del self.invetario[code]
            return True
        return False
            

    def get_stock(self, code: str) -> int:
        # TODO: implementar
        return self.invetario.get(code,0)

    def get_total_items(self) -> int:
        # TODO: implementar
        return sum(self.invetario.values())



# --- EJERCICIO 2: Contenedor de Sensores ---
# Contexto:
#   Un sistema recoge lecturas de sensores enteros y necesita estadísticas rápidas.
#
# Requerimientos:
#   - add_reading(value: int) → agrega lectura
#   - get_median() → mediana (si par, tomar el valor de la izquierda)
#   - get_average() → promedio
#   - reset() → borrar todas las lecturas
#
# Ejemplo:
# sd = SensorData()
# for r in [10,20,30,40]:
#     sd.add_reading(r)
# assert sd.get_median() == 20

class SensorData:
    def __init__(self):
        # TODO: inicializar estructuras internas
        self.sensores = []

    def add_reading(self, value: int):
        # TODO: implementar
        self.sensores.append(value)

    def get_median(self) -> float:
        # TODO: implementar

        if not self.sensores:
            return None

        ordenados = sorted(self.sensores)
        longitud = len(ordenados)//2
        if longitud%2== 0:
            return ordenados[longitud-1]
        else:
            return ordenados[longitud]

    def get_average(self) -> float:
        # TODO: implementar
        if not self.sensores:
            return None
        
        valor = 0
        for elem in self.sensores:
            valor += elem
        
        return valor/(len(self.sensores))

    def reset(self):
        # TODO: implementar
        self.sensores.clear()



# --- EJERCICIO 3: Planificación de Producción ---
# Contexto:
#   Se deben organizar órdenes de producción por prioridad.
#
# Requerimientos:
#   - add_order(order: str, priority: int) → añade orden
#   - pop_next() → obtiene y elimina orden más prioritaria
#   - list_orders() → devuelve órdenes en prioridad descendente
#
# Ejemplo:
# pp = ProductionPlanner()
# pp.add_order("Order1", 2)
# pp.add_order("Order2", 5)
# assert pp.pop_next() == "Order2"

class ProductionPlanner:
    def __init__(self):
        # TODO: inicializar estructuras internas
        self.ordenes = {}

    def add_order(self, order: str, priority: int):
        # TODO: implementar
        self.ordenes[order] = priority


    def pop_next(self) -> str:
        # TODO: implementar
        if not self.ordenes:
            return None
        
        highest = max(self.ordenes, key=lambda t:self.ordenes[t])
        del self.ordenes[highest]
        return highest

    def list_orders(self) -> list:
        # TODO: implementar
        return sorted(self.ordenes.keys(), key=lambda t: self.ordenes[t], reverse=True)



# --- EJERCICIO 4: Catálogo Versionado ---
# Contexto:
#   En un sistema de ventas, cada cambio al catálogo debe guardarse como versión.
#
# Requerimientos:
#   - Usa internamente un catálogo (dict o clase)
#   - Cada operación (add, remove, update) guarda snapshot
#   - Métodos:
#       add_product(name, price)
#       remove_product(name)
#       update_price(name, price)
#       get_version(i)
#       get_latest()
#
# Ejemplo:
# vc = VersionedCatalog()
# vc.add_product("Drill", 100)
# vc.update_price("Drill", 120)
# assert vc.get_version(0)["Drill"] == 100

class VersionedCatalog:
    def __init__(self):
        # Lista de versiones (snapshots completos del catálogo)
        self.versions = []
        self.current = {}

    def _save_version(self):
        # Guardar snapshot (copia profunda del catálogo actual)
        self.versions.append(self.current.copy())

    def add_product(self, name: str, price: float):
        self.current[name] = price
        self._save_version()

    def remove_product(self, name: str):
        if name in self.current:
            del self.current[name]
            self._save_version()

    def update_price(self, name: str, price: float):
        if name in self.current:
            self.current[name] = price
            self._save_version()

    def get_version(self, index: int) -> dict:
        if 0 <= index < len(self.versions):
            return self.versions[index]
        return {}

    def get_latest(self) -> dict:
        if not self.versions:
            return {}
        return self.versions[-1]



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
    for r in [10,20,30,40]:
        sd.add_reading(r)
    assert sd.get_median() == 20
    assert round(sd.get_average(),2) == 25
    sd.reset()
    assert sd.get_average() == None
    print("SensorData ✅")

def test_production_planner():
    pp = ProductionPlanner()
    pp.add_order("Order1", 2)
    pp.add_order("Order2", 5)
    pp.add_order("Order3", 3)
    assert pp.pop_next() == "Order2"
    assert pp.list_orders() == ["Order3","Order1"]
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
