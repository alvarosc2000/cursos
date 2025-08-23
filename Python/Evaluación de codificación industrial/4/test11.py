# =========================
# Simulacro ICA Industrial – Entry Level → Nivel 4
# =========================
# Tiempo sugerido: 90 minutos
# Objetivo: Practicar estructuras comunes (add/remove/get, medianas, prioridades)
# y en el Nivel 4 demostrar reutilización/refactorización/compatibilidad.
# =========================


# --- EJERCICIO 1: InventoryManager ---
# Enunciado:
# Implementa un inventario de productos.
# Debe permitir:
#  - añadir productos (sumando cantidad si ya existe)
#  - eliminar cierta cantidad (si llega a 0, se elimina del inventario)
#  - consultar la cantidad de un producto
#  - devolver todo el inventario
#
# Nota: Usar diccionario interno para gestionar {nombre: cantidad}

class InventoryManager:
    def __init__(self):
        """Inicializa un inventario vacío."""
        self.items = {}  # {nombre: cantidad}

    def add_item(self, name: str, quantity: int):
        # TODO: implementar
        if name in self.items:
            self.items[name] += quantity
        else:
            self.items[name] = quantity

    def remove_item(self, name: str, quantity: int):
        # TODO: implementar
        if name in self.items:
            self.items[name] -= quantity
            if self.items[name] < 0:
                del self.items[name]

    def get_quantity(self, name: str) -> int:
        # TODO: implementar
        return self.items.get(name,0)

    def get_all_items(self) -> dict:
        # TODO: implementar
        return self.items.copy()



# --- EJERCICIO 2: Container ---
# Enunciado:
# Implementa un contenedor de enteros que soporte:
#  - añadir valores
#  - borrar un valor (solo uno, si existe)
#  - obtener la mediana:
#       * si la lista es impar → el del medio
#       * si es par → el de la izquierda de los dos centrales
#
# Nota: Puedes usar una lista interna.

class Container:
    def __init__(self):
        self.data = []  # lista de enteros

    def add(self, value: int) -> None:
        # TODO: implementar
        self.data.append(value)

    def delete(self, value: int) -> bool:
        # TODO: implementar
        if value in self.data:
            self.data.remove(value)
            return True
        return False

    def get_median(self) -> int:
        # TODO: implementar
        if not self.data:
            return None
        ordenada = sorted(self.data)
        mid = len(ordenada) // 2

        if mid % 2 == 0:
            return ordenada[mid-1]
        else:
            return ordenada[mid]



# --- EJERCICIO 3: TaskScheduler ---
# Enunciado:
# Implementa un planificador de tareas con prioridades.
# Funcionalidades:
#   - añadir tarea con prioridad (entero)
#   - obtener la más prioritaria (y eliminarla de la lista)
#   - listar todas las tareas ordenadas por prioridad descendente

class TaskScheduler:
    def __init__(self):
        self.tasks = []  # lista de dicts {"task": str, "priority": int}

    def add_task(self, task: str, priority: int):
        # TODO: implementar
        self.tasks.append({"task":task,"priority":priority})

    def get_next_task(self) -> str:
        # TODO: implementar
        if not self.tasks:
            return "Vacia"
        
        highest = max(self.tasks, key=lambda t:t["priority"])
        self.tasks.remove(highest)
        return highest["task"]

    def get_all_tasks(self) -> list:
        # TODO: implementar
        sorted_tasks = sorted(self.tasks, key=lambda t: t["priority"], reverse=True)
        return [t["task"] for t in sorted_tasks]




# --- EJERCICIO 4: VersionedInventory (relacionado con Ej. 1) ---
# Enunciado:
# Ahora reutiliza y refactoriza el InventoryManager del Ejercicio 1
# para implementar un inventario con versiones:
#   - Cada vez que se modifique (add/remove), guarda una "versión"
#   - Permitir obtener una versión específica
#   - Permitir obtener la última versión
#
# Nota: Mantener compatibilidad con InventoryManager.
# Hint: Usa composición (un InventoryManager dentro de este).

class VersionedInventory:
    def __init__(self):
        self.manager = InventoryManager()
        self.versions = []  # lista de snapshots del inventario

    def _snapshot(self):
        # Guardamos una copia del estado actual del inventario
        self.versions.append(self.manager.get_all_items())

    def add_item(self, name: str, quantity: int):
        self.manager.add_item(name, quantity)
        self._snapshot()

    def remove_item(self, name: str, quantity: int):
        self.manager.remove_item(name, quantity)
        self._snapshot()

    def get_version(self, index: int) -> dict:
        if 0 <= index < len(self.versions):
            # Devolvemos copia para no exponer el estado interno
            return dict(self.versions[index])
        return None  # o {} si prefieres dict vacío

    def get_latest(self) -> dict:
        if not self.versions:
            return {}
        return dict(self.versions[-1])




# =========================
# TESTS DEL EXAMEN
# =========================

def test_inventory_manager():
    inv = InventoryManager()
    inv.add_item("peras", 10)
    inv.add_item("manzanas", 5)
    inv.add_item("peras", 2)
    assert inv.get_quantity("peras") == 12
    inv.remove_item("manzanas", 5)
    assert inv.get_quantity("manzanas") == 0
    print("InventoryManager ✅")

def test_container():
    c = Container()
    for v in [5, 3, 8, 2]:
        c.add(v)
    assert c.get_median() == 3
    c.delete(3)
    assert c.get_median() == 5
    print("Container ✅")

def test_task_scheduler():
    ts = TaskScheduler()
    ts.add_task("A", 1)
    ts.add_task("B", 3)
    ts.add_task("C", 2)
    assert ts.get_next_task() == "B"
    assert ts.get_all_tasks() == ["C", "A"]
    print("TaskScheduler ✅")

def test_versioned_inventory():
    vinv = VersionedInventory()
    vinv.add_item("peras", 5)
    vinv.add_item("manzanas", 2)
    vinv.remove_item("peras", 2)
    assert vinv.get_version(0)["peras"] == 5
    assert vinv.get_latest()["peras"] == 3
    print("VersionedInventory ✅")


if __name__ == "__main__":
    print("----- Simulacro ICA Industrial -----")
    test_inventory_manager()
    test_container()
    test_task_scheduler()
    test_versioned_inventory()
    print("\nTodos los tests completados ✅ ¡Examen simulado listo!")
