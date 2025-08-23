# =========================
# Simulacro ICA Industrial – Nivel 4
# =========================
# Tiempo sugerido: 90 minutos
# Objetivo: Evaluar codificación estructurada, clases, métodos y compatibilidad
# =========================

# --- EJERCICIO 1: ProductCatalog ---
# Enunciado:
# Implementa un catálogo de productos con:
#   - añadir producto (nombre, precio)
#   - eliminar producto por nombre
#   - actualizar precio de un producto
#   - obtener el producto más caro

class ProductCatalog:
    def __init__(self):
        # TODO: inicializar estructuras internas
        self.catalogo = []

    def add_product(self, name: str, price: float):
        # TODO: implementar
        self.catalogo.append({"name":name, "price":price})

    def remove_product(self, name: str):
        # TODO: implementar
        for prod in self.catalogo:
            if prod["name"] == name:
                self.catalogo.remove(prod)


    def update_price(self, name: str, price: float):
        # TODO: implementar
        for prod in self.catalogo:
            if prod["name"] == name:
                prod["price"] = price

    def get_most_expensive(self) -> dict:
        # TODO: implementar
        if not self.catalogo:
            return None
        return max(self.catalogo, key=lambda t: t["price"])


# --- EJERCICIO 2: NumberContainer ---
# Enunciado:
# Implementa un contenedor de números enteros con:
#   - añadir número
#   - eliminar un número (solo uno)
#   - obtener mediana
#   - obtener promedio

class NumberContainer:
    def __init__(self):
        # TODO: inicializar estructuras internas
        self.enteros = []

    def add_number(self, num: int):
        # TODO: implementar
        self.enteros.append(num)

    def remove_number(self, num: int) -> bool:
        # TODO: implementar
        if num in self.enteros:
            self.enteros.remove(num)
            return True
        return False

    def get_median(self) -> float:
        # TODO: implementar

        if not self.enteros:
            return None

        ordenadas = sorted(self.enteros)
        mid = len(ordenadas) // 2

        if mid % 2 == 0:
            return ordenadas[mid-1]
        else:
            return ordenadas[mid]
        
    def get_average(self) -> float:
        # TODO: implementar
        if not self.enteros:
            return None
        
        suma = 0
        for i in range(len(self.enteros)):
            suma += self.enteros[i]
        
        return suma/(len(self.enteros))


# --- EJERCICIO 3: TaskManager ---
# Enunciado:
# Implementa un planificador de tareas con prioridad:
#   - añadir tarea con prioridad
#   - obtener y eliminar tarea más prioritaria
#   - listar tareas por prioridad descendente

class TaskManager:
    def __init__(self):
        # TODO: inicializar estructuras internas
        self.tareas = []

    def add_task(self, task: str, priority: int):
        # TODO: implementar
        self.tareas.append({"task":task,"priority":priority})

    def pop_highest_priority(self) -> str:
        # TODO: implementar
        if not self.tareas:
            return None
        
        highest = max(self.tareas, key=lambda t:t["priority"])
        self.tareas.remove(highest)
        return highest["task"]

    def list_tasks(self) -> list:
        # TODO: implementar
        ordenada = sorted(self.tareas,key=lambda t:t["priority"])
        ordenada.reverse()
        return [t["task"] for t in ordenada]
        


# --- EJERCICIO 4: VersionedCatalog ---
# Enunciado:
# Reutiliza ProductCatalog para crear un catálogo con versiones:
#   - cada cambio (add, remove, update) guarda una versión
#   - obtener versión específica
#   - obtener última versión

class VersionedCatalog:
    def __init__(self):
        self.manager = ProductCatalog()
        self.versions = []  # lista de snapshots: dict nombre->precio

    def _snapshot(self):
        # Convertir lista de dicts a dict {name: price}
        snap = {}
        for prod in self.manager.catalogo:
            # si hay duplicados, el último con ese nombre prevalece
            snap[prod["name"]] = prod["price"]
        self.versions.append(snap)

    def add_product(self, name: str, price: float):
        self.manager.add_product(name, price)
        self._snapshot()

    def remove_product(self, name: str):
        self.manager.remove_product(name)
        self._snapshot()

    def update_price(self, name: str, price: float):
        self.manager.update_price(name, price)
        self._snapshot()

    def get_version(self, index: int) -> dict:
        if index < 0 or index >= len(self.versions):
            return None
        return self.versions[index]

    def get_latest(self) -> dict:
        if not self.versions:
            return None
        return self.versions[-1]


# =========================
# TESTS DEL SIMULACRO
# =========================

def test_product_catalog():
    pc = ProductCatalog()
    pc.add_product("Laptop", 1000)
    pc.add_product("Phone", 700)
    pc.update_price("Phone", 750)
    assert pc.get_most_expensive()["name"] == "Laptop"
    pc.remove_product("Laptop")
    assert pc.get_most_expensive()["name"] == "Phone"
    print("ProductCatalog ✅")


def test_number_container():
    nc = NumberContainer()
    for n in [4, 2, 7, 5]:
        nc.add_number(n)
    assert nc.get_median() == 4
    assert nc.get_average() == 4.5
    nc.remove_number(2)
    assert nc.get_median() == 5
    print("NumberContainer ✅")


def test_task_manager():
    tm = TaskManager()
    tm.add_task("A", 1)
    tm.add_task("B", 3)
    tm.add_task("C", 2)
    assert tm.pop_highest_priority() == "B"
    assert tm.list_tasks() == ["C", "A"]
    print("TaskManager ✅")


def test_versioned_catalog():
    vc = VersionedCatalog()
    vc.add_product("Tablet", 300)
    vc.add_product("Monitor", 200)
    vc.update_price("Tablet", 350)
    vc.remove_product("Monitor")
    assert vc.get_version(0)["Tablet"] == 300
    assert vc.get_latest()["Tablet"] == 350
    print("VersionedCatalog ✅")


if __name__ == "__main__":
    print("----- Simulacro ICA Industrial – Nuevo -----")
    test_product_catalog()
    test_number_container()
    test_task_manager()
    test_versioned_catalog()
    print("\nTodos los tests completados ✅ ¡Examen simulado listo!")
