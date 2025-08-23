# =========================
# Simulacro ICA Industrial – Nivel 4
# =========================
# Tiempo sugerido: 90 minutos
# Objetivo: Reutilización, refactorización y encapsulación.
# Cada ejercicio es independiente y debe ser implementado correctamente
# para pasar los tests al final.

# --- EJERCICIO 1: EmployeeManager ---
# Enunciado:
# Crea una clase EmployeeManager que gestione empleados con nombre y salario.
# Debe permitir añadir, eliminar empleados y obtener salario promedio
# y empleado con mayor salario. Código debe ser modular y compatible con futuras versiones.

class EmployeeManager:
    def __init__(self):
        """Inicializa la lista de empleados vacía."""
        self.employees = []  # lista de diccionarios: {"name": str, "salary": float}

    # BORRADOR: Métodos sin implementar aún
    def add_employee(self, name: str, salary: float):
        pass

    def remove_employee(self, name: str):
        pass

    def get_average_salary(self) -> float:
        pass

    def get_highest_salary(self) -> dict:
        pass


# --- EJERCICIO 2: TaskScheduler ---
# Enunciado:
# Crea una clase TaskScheduler que gestione tareas con prioridad.
# Debe permitir añadir tareas, obtener la siguiente más prioritaria
# y listar todas las tareas ordenadas por prioridad descendente.

class TaskScheduler:
    def __init__(self):
        """Inicializa la lista de tareas vacía."""
        self.tasks = []  # lista de diccionarios: {"task": str, "priority": int}

    # BORRADOR: Métodos sin implementar aún
    def add_task(self, task: str, priority: int):
        pass

    def get_next_task(self) -> str:
        pass

    def get_all_tasks(self) -> list:
        pass


# --- EJERCICIO 3: SensorSystem (Observer Pattern) ---
# Enunciado:
# Implementa un sistema de sensores que notifique alertas si un sensor supera un umbral.
# Permite suscribir funciones de alerta, agregar sensores y obtener el máximo valor.

class SensorSystem:
    def __init__(self, threshold: float):
        """Inicializa sistema de sensores con un umbral de alerta."""
        self.sensors = []  # lista de valores de sensores
        self.threshold = threshold
        self.subscribers = []  # funciones que se llaman cuando hay alerta

    # BORRADOR: Métodos sin implementar aún
    def add_sensor(self, value: float):
        pass

    def subscribe(self, func):
        pass

    def notify_alert(self, value: float):
        pass

    def get_max_sensor(self) -> float:
        pass


# --- EJERCICIO 4: VersionedStorage ---
# Enunciado:
# Implementa una clase VersionedStorage que guarde versiones de datos (diccionarios).
# Permite agregar nueva versión, obtener versión específica, y obtener última versión.
# Debe permitir compatibilidad con versiones anteriores al obtener datos.

class VersionedStorage:
    def __init__(self):
        self.versions = []  # lista de diccionarios

    # BORRADOR: Métodos sin implementar aún
    def add_version(self, data: dict):
        pass

    def get_version(self, index: int) -> dict:
        pass

    def get_latest(self) -> dict:
        pass


# =========================
# TESTS DEL SIMULACRO
# =========================

def test_employee_manager():
    mgr = EmployeeManager()
    mgr.add_employee("Alice", 5000)
    mgr.add_employee("Bob", 6000)
    mgr.add_employee("Charlie", 5500)
    assert mgr.get_average_salary() == (5000+6000+5500)/3
    assert mgr.get_highest_salary()["name"] == "Bob"
    mgr.remove_employee("Bob")
    assert mgr.get_highest_salary()["name"] == "Charlie"
    print("EmployeeManager tests passed ✅")


def test_task_scheduler():
    scheduler = TaskScheduler()
    scheduler.add_task("Write report", 2)
    scheduler.add_task("Fix bug", 5)
    scheduler.add_task("Email client", 3)
    assert scheduler.get_next_task() == "Fix bug"
    tasks = scheduler.get_all_tasks()
    assert tasks[0] == "Email client"
    assert tasks[1] == "Write report"
    print("TaskScheduler tests passed ✅")


def test_sensor_system():
    triggered = []

    def alert_func(value):
        triggered.append(value)

    sensors = SensorSystem(threshold=10.0)
    sensors.subscribe(alert_func)
    sensors.add_sensor(8)
    assert sensors.get_max_sensor() == 8
    assert triggered == []
    sensors.add_sensor(12)
    assert sensors.get_max_sensor() == 12
    assert triggered == [12]
    print("SensorSystem tests passed ✅")


def test_versioned_storage():
    storage = VersionedStorage()
    storage.add_version({"x": 1})
    storage.add_version({"x": 2, "y": 3})
    assert storage.get_latest()["x"] == 2
    assert storage.get_version(0)["x"] == 1
    print("VersionedStorage tests passed ✅")


# =========================
# EJECUCIÓN DE TESTS
# =========================
if __name__ == "__main__":
    print("----- Simulacro ICA Industrial – Nivel 4 -----")
    print("Tiempo sugerido: 90 minutos\n")
    test_employee_manager()
    test_task_scheduler()
    test_sensor_system()
    test_versioned_storage()
    print("\nTodos los tests completados ✅ ¡Simulacro listo!")
