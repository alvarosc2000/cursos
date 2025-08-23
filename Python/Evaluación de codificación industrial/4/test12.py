# =========================
# Simulacro ICA Industrial – Nuevo
# =========================
# Tiempo sugerido: 90 minutos
# Objetivo: Practicar estructuras comunes (add/remove/get, medianas, prioridades)
# Nivel 4: reutilización, refactorización y compatibilidad
# =========================


# --- EJERCICIO 1: StockManager ---
# Enunciado:
# Implementa un administrador de stock de productos.
# Funcionalidades:
#   - agregar stock (sumando si el producto ya existe)
#   - eliminar cantidad (si llega a 0, eliminar del inventario)
#   - consultar cantidad de un producto
#   - devolver inventario completo

class StockManager:
    def __init__(self):
        # TODO: inicializar estructuras internas
        self.items = {}

    def add_stock(self, name: str, quantity: int):
        # TODO: implementar
        if name in self.items:
            self.items[name] += quantity
        else:
            self.items[name] = quantity

    def remove_stock(self, name: str, quantity: int):
        # TODO: implementar
        if name in self.items:
            self.items[name] -= quantity
            if self.items[name] <= 0:
                del self.items[name]

    def get_quantity(self, name: str) -> int:
        # TODO: implementar
        return self.items.get(name,0)

    def get_inventory(self) -> dict:
        # TODO: implementar
        return self.items.copy()



# --- EJERCICIO 2: MedianContainer ---
# Enunciado:
# Contenedor de enteros que soporte:
#   - añadir valores
#   - eliminar valor (solo una vez si existe)
#   - calcular mediana (si par, el de la izquierda)

class MedianContainer:
    def __init__(self):
        # TODO: inicializar estructuras internas
        self.values = []

    def add_number(self, value: int):
        # TODO: implementar
        self.values.append(value)

    def remove_number(self, value: int) -> bool:
        # TODO: implementar
        if not self.values:
            return False
        return self.values.remove(value)

    def get_median(self) -> int:
        # TODO: implementar

        if not self.values:
            return None

        ordenados = sorted(self.values)
        mid = len(ordenados)//2

        if mid % 2 == 0:
            return ordenados[mid-1]
        else:
            return ordenados[mid]



# --- EJERCICIO 3: PriorityQueue ---
# Enunciado:
# Cola de prioridades:
#   - añadir elemento con prioridad
#   - obtener elemento con mayor prioridad (y eliminarlo)
#   - listar todos los elementos ordenados por prioridad descendente

class PriorityQueue:
    def __init__(self):
        # TODO: inicializar estructuras internas
        self.cola = []

    def add_item(self, item: str, priority: int):
        # TODO: implementar
        self.cola.append({"item":item,"priority":priority})

    def pop_highest(self) -> str:
        # TODO: implementar
        if not self.cola:
            return None
        highest = max(self.cola,key=lambda t:t["priority"])
        self.cola.remove(highest)
        return highest["item"]

    def list_items(self) -> list:
        # TODO: implementar
        ordenada = sorted(self.cola, key=lambda t:t["priority"])
        ordenada.reverse()
        return [t["item"] for t in ordenada]



# --- EJERCICIO 4: VersionedStock (relacionado con Ej.1) ---
# Enunciado:
# Reutiliza StockManager para implementar un inventario con versiones:
#   - guardar versión cada vez que se modifica
#   - obtener versión específica
#   - obtener última versión
# Debe mantener compatibilidad con StockManager

class VersionedStock:
    def __init__(self):
        # TODO: inicializar estructuras internas
        self.manager = StockManager()
        self.versions = []

    def _snapshot(self):
        self.versions.append(self.manager.get_inventory())

    def add_stock(self, name: str, quantity: int):
        # TODO: implementar
        self.manager.add_stock(name,quantity)
        self._snapshot()

    def remove_stock(self, name: str, quantity: int):
        # TODO: implementar
        self.manager.remove_stock(name,quantity)
        self._snapshot()

    def get_version(self, index: int) -> dict:
        # TODO: implementar
        if index >= 0 or index < len(self.versions):
            return dict(self.versions[index])
        return None
    
    def get_latest(self) -> dict:
        # TODO: implementar
        if not self.versions:
            return {}
        return dict(self.versions[-1])



# =========================
# TESTS DEL SIMULACRO
# =========================

def test_stock_manager():
    sm = StockManager()
    sm.add_stock("peras", 10)
    sm.add_stock("manzanas", 5)
    sm.add_stock("peras", 2)
    assert sm.get_quantity("peras") == 12
    sm.remove_stock("manzanas", 5)
    assert sm.get_quantity("manzanas") == 0
    print("StockManager ✅")

def test_median_container():
    mc = MedianContainer()
    for v in [5, 3, 8, 2]:
        mc.add_number(v)
    assert mc.get_median() == 3
    mc.remove_number(3)
    assert mc.get_median() == 5
    print("MedianContainer ✅")

def test_priority_queue():
    pq = PriorityQueue()
    pq.add_item("A", 1)
    pq.add_item("B", 3)
    pq.add_item("C", 2)
    assert pq.pop_highest() == "B"
    assert pq.list_items() == ["C", "A"]
    print("PriorityQueue ✅")

def test_versioned_stock():
    vs = VersionedStock()
    vs.add_stock("peras", 5)
    vs.add_stock("manzanas", 2)
    vs.remove_stock("peras", 2)
    assert vs.get_version(0)["peras"] == 5
    assert vs.get_latest()["peras"] == 3
    print("VersionedStock ✅")

if __name__ == "__main__":
    print("----- Simulacro ICA Industrial – Nuevo -----")
    test_stock_manager()
    test_median_container()
    test_priority_queue()
    test_versioned_stock()
    print("\nTodos los tests completados ✅ ¡Examen simulado listo!")
