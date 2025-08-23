# =========================
# EXAMEN SIMULADO INDUSTRIAL – Todo en una clase
# =========================
# Objetivo: Evaluar codificación estructurada, OOP y manejo de colecciones
# Nivel: Entry-Level alto / Mid
# Tiempo sugerido: 90 min
# Lenguaje: Python 3
# =========================

class IndustrialExam:
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
            self.inventario = {}

        def add_item(self, code: str, quantity: int):
            # Agregar piezas al inventario. Si code existe, sumar cantidad.
            # Si quantity <= 0, lanzar ValueError
            if quantity <= 0:
                raise ValueError("Cantidad negativa")
            if code in self.inventario:
                self.inventario[code] += quantity
            else:
                self.inventario[code] = quantity

        def remove_item(self, code: str, quantity: int) -> bool:
            # Restar piezas del inventario, retornar True si se eliminaron
            # Si no hay suficientes, retornar False
            if code in self.inventario and self.inventario[code] >= quantity:
                self.inventario[code] -= quantity
                return True
            return False

        def get_stock(self, code: str) -> int:
            # Retornar cantidad actual del código. Si no existe, retornar 0
            return self.inventario.get(code,0)

        def get_total_items(self) -> int:
            # Retornar suma total de todas las piezas
            return sum(self.inventario.values())

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
            # Agregar lectura. Si value <= 0, lanzar ValueError
            if value <=  0:
                raise ValueError("Valor negativo")
            else:
                self.lecturas.append(value)

        def get_median(self) -> float:
            if not self.lecturas:
                raise RuntimeError("Lista vacía")
            
            ordenado = sorted(self.lecturas)
            n = len(ordenado)
            mid = n // 2
            
            if n % 2 == 0:          # longitud par
                return ordenado[mid-1]  # elemento izquierdo
            else:
                return ordenado[mid]    # longitud impar



        def get_average(self) -> float:
            # Retornar promedio de lecturas. Si vacío, retornar None
            if not self.lecturas:
                return None
            else:
                total = 0
                for elem in self.lecturas:
                    total += elem
                return total/(len(self.lecturas))

        def reset(self):
            # Limpiar todas las lecturas
            return self.lecturas.clear()

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
            # Agregar orden con prioridad (mayor = más urgente)
            # Validar que order no esté vacío y priority >= 0
            if not order:
                raise ValueError("Orden no puede ser vacía")
            if priority < 0:
                raise ValueError("La prioridad debe ser >= 0")
            self.ordenes[order] = priority                 

        def pop_next(self) -> str:
            # Extraer y retornar orden de mayor prioridad
            # Si está vacío, lanzar RuntimeError
            if not self.ordenes:
                raise RuntimeError("Error")
            
            highest = max(self.ordenes, key=lambda t:self.ordenes[t])
            del self.ordenes[highest]
            return highest

        def list_orders(self) -> list:
            # Retornar lista de órdenes actuales por prioridad descendente
            return sorted(self.ordenes, key=lambda t:self.ordenes[t], reverse=True)

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
            # Guardar snapshot de productos actuales
            self.versiones.append(self.productos.copy())

        def add_product(self, name: str, price: float):
            # Agregar producto nuevo. Si existe, lanzar RuntimeError
            # Luego guardar snapshot
            if name in self.productos:
                raise RuntimeError("producto existente")
            else:
                self.productos[name] = price
                self._save_version()

        def remove_product(self, name: str):
            # Eliminar producto. Si no existe, lanzar KeyError
            # Luego guardar snapshot
            if name not in self.productos:
                raise KeyError("Error, producto no encontrado")
            else:
                del self.productos[name]
                self._save_version()

        def update_price(self, name: str, price: float):
            # Actualizar precio de producto existente. Si no existe, KeyError
            # Luego guardar snapshot
            if name not in self.productos:
                raise KeyError("Error, producto no encontrado")
            else:
                self.productos[name] = price
                self._save_version()

        def get_version(self, index: int) -> dict:
            # Retornar copia de la versión index. Si inválido, IndexError
            if index < 0 or index >= len(self.versiones):
                raise IndexError("Indice erroneo")
            else:
                return self.versiones[index].copy()

        def get_latest(self) -> dict:
            # Retornar última versión registrada. Si no hay versiones, RuntimeError
            if not self.versiones:
                raise RuntimeError("No versiones")
            return self.versiones[-1].copy()
        
        def get_maximo_versiones(self) -> int:
            ordenada = sorted(self.versiones)
            return ordenada[-1]


# =========================
# TESTS DEL EXAMEN
# =========================
def run_tests():
    print("=== TESTS INDUSTRIAL EXAM ===")

    # --- Inventory ---
    inv = IndustrialExam.Inventory()
    inv.add_item("BOLT", 50)
    inv.add_item("BOLT", 10)
    assert inv.get_stock("BOLT") == 60
    assert inv.remove_item("BOLT", 20) is True
    assert inv.get_stock("BOLT") == 40
    assert inv.remove_item("BOLT", 100) is False
    print("Inventory ✅")

    # --- SensorData ---
    sd = IndustrialExam.SensorData()
    for r in [10, 20, 30, 40]:
        sd.add_reading(r)
    # Solo se valida que el método devuelva algo; completarlo tú
    print("SensorData: get_median =", sd.get_median())
    print("SensorData: get_average =", sd.get_average())
    sd.reset()
    assert sd.get_average() is None
    print("SensorData ✅")

    # --- ProductionPlanner ---
    pp = IndustrialExam.ProductionPlanner()
    pp.add_order("Order1", 2)
    pp.add_order("Order2", 5)
    pp.add_order("Order3", 3)
    # Validar método pop_next y list_orders
    print("ProductionPlanner: pop_next =", pp.pop_next())
    print("ProductionPlanner: list_orders =", pp.list_orders())
    print("ProductionPlanner ✅")

    # --- VersionedCatalog ---
    vc = IndustrialExam.VersionedCatalog()
    vc.add_product("Drill", 100)
    vc.update_price("Drill", 120)
    vc.add_product("Hammer", 50)
    vc.remove_product("Hammer")
    # Validar get_version y get_latest
    print("VersionedCatalog: latest =", vc.get_latest())
    print("VersionedCatalog: version 0 =", vc.get_version(0))
    print("VersionedCatalog ✅")

    print("Todos los tests listos ✅")


if __name__ == "__main__":
    run_tests()
