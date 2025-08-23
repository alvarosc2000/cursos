"""
=========================================
   EXAMEN DE PRÁCTICA - CODIFICACIÓN INDUSTRIAL
   CodeSignal ICA (Entry-Level → Mid-Level)
=========================================

Duración sugerida: 90 minutos.
Reglas:
 - No modificar enunciados ni cabeceras.
 - Implementa cada método exactamente como se pide.
 - Maneja casos límite: estructuras vacías, valores inválidos, elementos inexistentes.
 - Si la operación no puede completarse, debes lanzar una excepción.
 - Usa estructuras internas eficientes cuando corresponda.
 - Todos los tests al final deben pasar.

Excepciones recomendadas:
 - ValueError: cuando un argumento no es válido.
 - KeyError: cuando un elemento solicitado no existe.
 - RuntimeError: cuando la operación no puede realizarse por estado inconsistente.

"""

# =========================
# EJERCICIO 1: Contenedor de Sensores
# =========================
class SensorContainer:
    """
    Gestiona lecturas de sensores industriales.

    Requisitos:
      - add_reading(value: int) -> None
          Agrega una lectura. El valor debe ser un entero positivo.
          Si value <= 0, lanzar ValueError.

      - remove_reading(value: int) -> bool
          Elimina una ocurrencia del valor. Devuelve True si se eliminó,
          False si no existe.

      - get_median() -> int
          Devuelve la mediana de las lecturas actuales.
          Si está vacío, lanzar RuntimeError.

      - get_latest() -> int
          Devuelve la última lectura agregada.
          Si está vacío, lanzar RuntimeError.
    """
    def __init__(self):
        self.readings = []

    def add_reading(self, value: int) -> None:
        if value <=0:
            raise ValueError("Valor debe ser positivo")
        self.readings.append(value)


    def remove_reading(self, value: int) -> bool:
        if value in self.readings:
            self.readings.remove(value)
            return True
        return False

    def get_median(self) -> int:
        if not self.readings:
            raise RuntimeError("No hay lecturas registradas")
        ordenados = sorted(self.readings)
        n = len(ordenados)
        mid = n // 2
        if n % 2 == 1:
            return ordenados[mid]
        else:
            return (ordenados[mid - 1] + ordenados[mid]) // 2

    def get_latest(self) -> int:
        if not self.readings:
            raise RuntimeError("No hay lecturas registradas")
        return self.readings[-1]


# =========================
# EJERCICIO 2: Inventario de Almacén
# =========================
class WarehouseInventory:
    """
    Controla productos en un almacén.

    Requisitos:
      - add_item(name: str, qty: int)
          Agrega unidades de un producto.
          name no puede estar vacío.
          qty debe ser > 0, de lo contrario lanzar ValueError.

      - remove_item(name: str, qty: int) -> bool
          Resta unidades. Si el producto no existe, lanzar KeyError.
          Si qty > stock disponible, lanzar RuntimeError.
          Devuelve True si se eliminó correctamente.

      - get_stock(name: str) -> int
          Devuelve stock actual. Si no existe, devolver 0.

      - list_inventory() -> dict
          Devuelve copia del inventario actual.
    """
    def __init__(self):
        self.inventory = {}

    def add_item(self, name: str, qty: int):
        if qty < 0:
            raise RuntimeError("Cantidad negativa")
        if name in self.inventory:
            self.inventory[name] += qty
        else:
            self.inventory[name] = qty

    def remove_item(self, name: str, qty: int) -> bool:
        if name not in self.inventory:
            raise KeyError("Producto no existe")
        if qty > self.inventory[name]:
            raise RuntimeError("Cantidad mayor a la disponible")
        self.inventory[name] -= qty
        return True

    def get_stock(self, name: str) -> int:
        return self.inventory.get(name,0)

    def list_inventory(self) -> dict:
        return self.inventory.copy()


# =========================
# EJERCICIO 3: Planificación de Producción
# =========================
class ProductionPlanner:
    """
    Gestiona órdenes de producción con prioridades.

    Requisitos:
      - add_order(order: str, priority: int)
          Inserta una orden con prioridad (entero, mayor = más urgente).
          order no puede ser vacío. priority debe ser >= 0.

      - pop_next() -> str
          Extrae y devuelve la orden de mayor prioridad.
          Si está vacío, lanzar RuntimeError.

      - list_orders() -> list
          Devuelve una lista con todas las órdenes actuales
          (solo nombres, no prioridades).
    """
    def __init__(self):
        self.orders = {}

    def add_order(self, order: str, priority: int):
        if not order:
            raise ValueError("Orden no puede ser vacía")
        if priority < 0:
            raise ValueError("La prioridad debe ser >= 0")
        self.orders[order] = priority

    def pop_next(self) -> str:
        if not self.orders:
            raise RuntimeError("Diccionario vacio")
        
        highest = max(self.orders, key=lambda t:self.orders[t])
        del self.orders[highest]
        return highest

    def list_orders(self) -> list:
        return list(self.orders.keys())


# =========================
# EJERCICIO 4: Catálogo con Versionado
# =========================
class VersionedCatalog:
    """
    Catálogo de productos con control de versiones.

    Requisitos:
      - add_product(name: str, price: float)
          Inserta un producto nuevo. Si ya existe, lanzar RuntimeError.
          Luego guarda un snapshot de la versión.

      - remove_product(name: str)
          Elimina un producto. Si no existe, lanzar KeyError.
          Luego guarda un snapshot de la versión.

      - update_price(name: str, price: float)
          Actualiza precio de un producto existente.
          Si no existe, lanzar KeyError.
          Luego guarda un snapshot de la versión.

      - get_version(index: int) -> dict
          Devuelve copia de la versión index.
          Si index es inválido, lanzar IndexError.

      - get_latest() -> dict
          Devuelve la última versión registrada.
          Si no hay versiones, lanzar RuntimeError.
    """
    def __init__(self):
        self.products = {}
        self.versions = []

    def _save_version(self):
        # Guardamos copia profunda (snapshot inmutable de ese estado)
        self.versions.append(self.products.copy())

    def add_product(self, name: str, price: float):
        if name in self.products:
            raise RuntimeError(f"El producto '{name}' ya existe")
        self.products[name] = price
        self._save_version()

    def remove_product(self, name: str):
        if name not in self.products:
            raise KeyError(f"El producto '{name}' no existe")
        del self.products[name]
        self._save_version()

    def update_price(self, name: str, price: float):
        if name not in self.products:
            raise KeyError(f"El producto '{name}' no existe")
        self.products[name] = price
        self._save_version()

    def get_version(self, index: int) -> dict:
        if index < 0 or index >= len(self.versions):
            raise IndexError("Índice de versión inválido")
        return self.versions[index].copy()

    def get_latest(self) -> dict:
        if not self.versions:
            raise RuntimeError("No hay versiones registradas")
        return self.versions[-1].copy()

# =========================
# TESTS UNITARIOS
# =========================
def run_tests():
    print("=== TESTS EJERCICIO 1 ===")
    s = SensorContainer()
    s.add_reading(10); s.add_reading(20); s.add_reading(30)
    assert s.get_latest() == 30
    assert s.get_median() == 20
    assert s.remove_reading(20) is True
    assert s.remove_reading(99) is False
    try:
        SensorContainer().get_latest()
    except RuntimeError: pass
    try:
        s.add_reading(-5)
    except ValueError: pass

    print("=== TESTS EJERCICIO 2 ===")
    w = WarehouseInventory()
    w.add_item("tornillo", 50)
    assert w.get_stock("tornillo") == 50
    assert w.remove_item("tornillo", 20) is True
    try:
        w.remove_item("tuerca", 5)
    except KeyError: pass
    try:
        w.remove_item("tornillo", 999)
    except RuntimeError: pass
    try:
        w.add_item("", 10)
    except ValueError: pass

    print("=== TESTS EJERCICIO 3 ===")
    p = ProductionPlanner()
    p.add_order("motor", 2)
    p.add_order("cinta", 5)
    p.add_order("panel", 1)
    assert p.pop_next() == "cinta"
    assert sorted(p.list_orders()) == ["motor", "panel"]
    try:
        ProductionPlanner().pop_next()
    except RuntimeError: pass

    print("=== TESTS EJERCICIO 4 ===")
    c = VersionedCatalog()
    c.add_product("robot", 1000.0)
    c.update_price("robot", 1200.0)
    c.add_product("sensor", 200.0)
    assert "robot" in c.get_latest()
    v0 = c.get_version(0)
    assert v0["robot"] == 1000.0
    v1 = c.get_version(1)
    assert v1["robot"] == 1200.0
    try:
        c.add_product("robot", 1500.0)
    except RuntimeError: pass
    try:
        c.get_version(999)
    except IndexError: pass

    print("✅ Todos los tests pasaron correctamente")


if __name__ == "__main__":
    run_tests()
