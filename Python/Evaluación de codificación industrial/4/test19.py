# =========================
# EXAMEN COMPLETO SIMULADO – Todo en una clase
# =========================
# Objetivo: Evaluar codificación estructurada, OOP, manejo de colecciones
# Nivel: Entry-Level alto / Mid
# Tiempo sugerido: 90 min
# Lenguaje: Python 3
# =========================

class IndustrialExamFull:
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
              # Agrega piezas al inventario
          - remove_item(code: str, quantity: int) -> bool
              # Elimina piezas si hay suficiente stock
          - get_stock(code: str) -> int
              # Retorna cantidad actual
          - get_total_items() -> int
              # Retorna total de todas las piezas
          - list_items() -> list
              # Retorna lista de códigos existentes
        """
        def __init__(self):
            self.inventario = {}

        def add_item(self, code: str, quantity: int):
            if code in self.inventario:
                self.inventario[code] += quantity
            else:
                self.inventario[code] = quantity

        def remove_item(self, code: str, quantity: int) -> bool:
            if code in self.inventario and quantity <= self.inventario[quantity]:
                self.inventario[code] -= quantity
                return True
            return False

        def get_stock(self, code: str) -> int:
            return self.inventario.get(code,0)

        def get_total_items(self) -> int:
            return sum(self.inventario.values())

        def list_items(self) -> list:
            return self.inventario.copy()

    # =========================
    # EJERCICIO 2: Contenedor de Sensores
    # =========================
    class SensorData:
        """
        Contenedor de lecturas de sensores.
        Métodos a implementar:
          - add_reading(value: int)
              # Agrega lectura, valor positivo
          - remove_reading(value: int) -> bool
              # Elimina una ocurrencia
          - get_median() -> float
              # Devuelve mediana
          - get_average() -> float
              # Devuelve promedio
          - get_latest() -> int
              # Devuelve última lectura
          - reset()
              # Limpia todas las lecturas
        """
        def __init__(self):
            self.lecturas = []

        def add_reading(self, value: int):
            if value >= 0:
                self.lecturas.append(value)
            else:
                raise ValueError("Valor negativo")

        def remove_reading(self, value: int) -> bool:
            for i in range (len(self.lecturas)):
                if self.lecturas[i] == value:
                    self.lecturas.remove(value)
                    return True
            return False
                
        def get_median(self) -> float:
            if not self.lecturas:
                return None
            else:
                ordenados = sorted(self.lecturas)
                n = len(ordenados)
                mitad = n // 2

                if mitad % 2 == 0:
                    return ordenados[mitad-1]
                else:
                    return ordenados[mitad]

        def get_average(self) -> float:
            if not self.lecturas:
                return None
            else:
                total = 0
                for i in range(len(self.lecturas)):
                    total += self.lecturas[i]
                return total/(len(self.lecturas))

        def get_latest(self) -> int:
            return self.lecturas[-1]

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
              # Agrega orden con prioridad (mayor = más urgente)
          - pop_next() -> str
              # Extrae orden más urgente
          - list_orders() -> list
              # Lista todas las órdenes
          - update_priority(order: str, priority: int)
              # Cambia prioridad de orden existente
          - remove_order(order: str) -> bool
              # Elimina orden específica
        """
        def __init__(self):
            self.ordenes = {}

        def add_order(self, order: str, priority: int):
            if not order:
                raise ValueError("Orden no puede ser vacía")
            if priority < 0:
                raise ValueError("La prioridad debe ser >= 0")
            self.ordenes[order] = priority      

        def pop_next(self) -> str:
            if not self.ordenes:
                raise RuntimeError("error")
            else:
                highest = max(self.ordenes, key=lambda t:self.ordenes[t])
                del self.ordenes[highest]
                return highest

        def list_orders(self) -> list:
            if not self.ordenes:
                raise ValueError("Vacia")
            else:
                return sorted(self.ordenes, key=lambda t:self.ordenes[t], reverse=True)

        def update_priority(self, order: str, priority: int):
            if order in self.ordenes:
                self.ordenes[order] = priority
            else:
                self.ordenes[order] = priority 

        def remove_order(self, order: str) -> bool:
            if order in self.ordenes:
                del self.ordenes[order]
                return True
            return False

    # =========================
    # EJERCICIO 4: Catálogo Versionado
    # =========================
    class VersionedCatalog:
        """
        Catálogo de productos con control de versiones.
        Métodos a implementar:
          - add_product(name: str, price: float)
              # Inserta producto
          - remove_product(name: str)
              # Elimina producto existente
          - update_price(name: str, price: float)
              # Actualiza precio de producto existente
          - get_version(index: int) -> dict
              # Devuelve snapshot de versión específica
          - get_latest() -> dict
              # Devuelve snapshot más reciente
          - list_products() -> list
              # Lista todos los productos actuales
          - find_product(name: str) -> bool
              # Retorna True si producto existe
        """
        def __init__(self):
            self.productos = {}
            self.versiones = []

        def _save_version(self):
            self.versiones.append(self.productos.copy())

        def add_product(self, name: str, price: float):
            self.productos[name] = price
            

        def remove_product(self, name: str):
            pass

        def update_price(self, name: str, price: float):
            pass

        def get_version(self, index: int) -> dict:
            pass

        def get_latest(self) -> dict:
            pass

        def list_products(self) -> list:
            pass

        def find_product(self, name: str) -> bool:
            pass

# =========================
# TESTS DEL EXAMEN
# =========================
def run_tests():
    print("=== TESTS INDUSTRIAL EXAM FULL ===")

    # Inventory
    inv = IndustrialExamFull.Inventory()
    inv.add_item("BOLT", 50)
    inv.add_item("NUT", 30)
    print("Inventory list:", inv.list_items())

    # SensorData
    sd = IndustrialExamFull.SensorData()
    sd.add_reading(10)
    sd.add_reading(20)
    print("Sensor latest:", sd.get_latest())

    # ProductionPlanner
    pp = IndustrialExamFull.ProductionPlanner()
    pp.add_order("Order1", 2)
    pp.add_order("Order2", 5)
    print("Next order:", pp.pop_next())
    print("Orders list:", pp.list_orders())

    # VersionedCatalog
    vc = IndustrialExamFull.VersionedCatalog()
    vc.add_product("Drill", 100)
    vc.update_price("Drill", 120)
    print("Latest catalog:", vc.get_latest())
    print("Version 0:", vc.get_version(0))

    print("Tests listos ✅")

if __name__ == "__main__":
    run_tests()
