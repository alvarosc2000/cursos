# =========================
# EXAMEN SIMULADO INDUSTRIAL – Todo en una clase
# =========================
# Objetivo: Evaluar codificación estructurada, OOP y manejo de colecciones
# Nivel: Entry-Level alto / Mid
# Tiempo sugerido: 90 min
# Lenguaje: Python 3
# =========================

class IndustrialSystem:
    """
    Sistema completo para práctica de codificación industrial ICA.
    Contiene:
      1) Inventario de piezas
      2) Contenedor de lecturas de sensores
      3) Planificador de producción
      4) Catálogo de productos versionado
    """

    # =========================
    # EJERCICIO 1: Inventario de Piezas
    # =========================
    class Inventory:
        """
        Inventario digital de piezas de repuesto.
        Métodos a implementar:
          - add_item(code: str, quantity: int)
          - remove_item(code: str, quantity: int) -> bool
          - get_stock(code: str) -> int
          - get_total_items() -> int
        """
        def __init__(self):
            self.invetario = {}

        def add_item(self, code: str, quantity: int):
            if code in self.invetario:
                self.invetario[code] += quantity
            else:
                self.invetario[code] = quantity

        def remove_item(self, code: str, quantity: int) -> bool:
            if code in self.invetario and self.invetario[code]>=quantity:
                self.invetario[code] -= quantity
                if self.invetario[code] == 0:
                    del self.invetario[code]
                return True
            return False

        def get_stock(self, code: str) -> int:
            return self.invetario.get(code,0)

        def get_total_items(self) -> int:
            return sum(self.invetario.values())

    # =========================
    # EJERCICIO 2: Contenedor de Sensores
    # =========================
    class SensorData:
        """
        Contenedor de lecturas enteras de sensores.
        Métodos a implementar:
          - add_reading(value: int)
          - get_median() -> float
          - get_average() -> float
          - reset()
        """
        def __init__(self):
            self.lecturas = []

        def add_reading(self, value: int):
            self.lecturas.append(value)

        def get_median(self) -> float:
            if not self.lecturas:
                return None
            
            ordenados = sorted(self.lecturas)
            mitad = len(ordenados)//2

            if mitad % 2 == 0:
                return ordenados[mitad-1]
            else:
                return ordenados[mitad]

        def get_average(self) -> float:
            if not self.lecturas:
                return None
            
            t = 0
            for i in self.lecturas:
                t += i
            
            return t/(len(self.lecturas))

        def reset(self):
            self.lecturas.clear()

    # =========================
    # EJERCICIO 3: Planificación de Producción
    # =========================
    class ProductionPlanner:
        """
        Gestiona órdenes de producción con prioridades.
        Métodos a implementar:
          - add_order(order: str, priority: int)
          - pop_next() -> str
          - list_orders() -> list
        """
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
            return sorted(self.ordenes.keys(),key=lambda t:self.ordenes[t], reverse=True)

    # =========================
    # EJERCICIO 4: Catálogo Versionado
    # =========================
    class VersionedCatalog:
        """
        Catálogo de productos con control de versiones.
        Métodos a implementar:
          - add_product(name: str, price: float)
          - remove_product(name: str)
          - update_price(name: str, price: float)
          - get_version(index: int) -> dict
          - get_latest() -> dict
        """
        def __init__(self):
            self.productos = {}
            self.versiones = []

        def _save_version(self):
            self.versiones.append(self.productos.copy())

        def add_product(self, name: str, price: float):
            self.productos[name] = price
            self._save_version()

        def remove_product(self, name: str):
            if name in self.productos:
                del self.productos[name]
                self._save_version()

        def update_price(self, name: str, price: float):
            if name in self.productos:
                self.productos[name] = price
                self._save_version()

        def get_version(self, index: int) -> dict:
            if index <= len(self.versiones) or index >= 0:
                return self.versiones[index]
            return {}

        def get_latest(self) -> dict:
            if not self.versiones:
                return {}
            return self.versiones[-1]


# =========================
# TESTS DEL SIMULACRO
# =========================
def run_tests():
    print("Ejecutando tests ICA simulacro...")

    # --- Inventory ---
    inv = IndustrialSystem.Inventory()
    inv.add_item("BOLT", 50)
    inv.add_item("BOLT", 10)
    assert inv.get_stock("BOLT") == 60
    assert inv.remove_item("BOLT", 20) == True
    assert inv.get_stock("BOLT") == 40
    assert inv.remove_item("BOLT", 100) == False
    print("Inventory ✅")

    # --- SensorData ---
    sd = IndustrialSystem.SensorData()
    for r in [10, 20, 30, 40]:
        sd.add_reading(r)
    assert sd.get_median() == 20
    assert round(sd.get_average(),2) == 25
    sd.reset()
    assert sd.get_average() is None
    print("SensorData ✅")

    # --- ProductionPlanner ---
    pp = IndustrialSystem.ProductionPlanner()
    pp.add_order("Order1", 2)
    pp.add_order("Order2", 5)
    pp.add_order("Order3", 3)
    assert pp.pop_next() == "Order2"
    assert pp.list_orders() == ["Order3","Order1"]
    print("ProductionPlanner ✅")

    # --- VersionedCatalog ---
    vc = IndustrialSystem.VersionedCatalog()
    vc.add_product("Drill", 100)
    vc.add_product("Hammer", 50)
    vc.update_price("Drill", 120)
    vc.remove_product("Hammer")
    assert vc.get_version(0)["Drill"] == 100
    assert vc.get_latest()["Drill"] == 120
    print("VersionedCatalog ✅")

    print("Todos los tests listos ✅")

if __name__ == "__main__":
    run_tests()
