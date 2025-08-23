# =========================
# Simulacro ICA Industrial – Nivel 4 (Completo)
# =========================
# Tiempo sugerido: 90 minutos
# Objetivo: Reutilización, refactorización y encapsulación.
# Cada ejercicio es independiente y debe ser implementado correctamente
# para pasar los tests al final.

# --- EJERCICIO 1: EmployeeManager ---
class EmployeeManager:
    def __init__(self):
        """Inicializa la lista de empleados vacía."""
        self.employees = []  # lista de diccionarios: {"name": str, "salary": float}

    def add_employee(self, name: str, salary: float):
        """Agrega un empleado o actualiza su salario si ya existe."""
        for emp in self.employees:
            if emp["name"] == name:
                emp["salary"] = salary
                return
        self.employees.append({"name": name, "salary": salary})

    def remove_employee(self, name: str):
        """Elimina un empleado por nombre."""
        self.employees = [emp for emp in self.employees if emp["name"] != name]

    def get_average_salary(self) -> float:
        """Devuelve el salario promedio de los empleados."""
        if not self.employees:
            return 0.0
        total = sum(emp["salary"] for emp in self.employees)
        return total / len(self.employees)

    def get_highest_salary(self) -> dict:
        """Devuelve el empleado con el salario más alto."""
        if not self.employees:
            return None
        return max(self.employees, key=lambda emp: emp["salary"])


# --- EJERCICIO 2: TaskScheduler ---
class TaskScheduler:
    def __init__(self):
        """Inicializa la lista de tareas vacía."""
        self.tasks = []  # lista de diccionarios: {"task": str, "priority": int}

    def add_task(self, task: str, priority: int):
        """Agrega una tarea con prioridad. Prioridad más alta = más importante."""
        self.tasks.append({"task": task, "priority": priority})

    def get_next_task(self) -> str:
        """Devuelve la tarea más prioritaria y la elimina de la lista."""
        if not self.tasks:
            return None
        highest = max(self.tasks, key=lambda t: t["priority"])
        self.tasks.remove(highest)
        return highest["task"]

    def get_all_tasks(self) -> list:
        """Devuelve todas las tareas ordenadas por prioridad descendente."""
        return [t["task"] for t in sorted(self.tasks, key=lambda t: t["priority"], reverse=True)]


# --- EJERCICIO 3: SensorSystem (Observer Pattern) ---
class SensorSystem:
    def __init__(self, threshold: float):
        """Inicializa sistema de sensores con un umbral de alerta."""
        self.sensors = []  # lista de valores de sensores
        self.threshold = threshold
        self.subscribers = []  # funciones que se llaman cuando hay alerta

    def add_sensor(self, value: float):
        """Agrega un sensor y notifica si supera el umbral."""
        self.sensors.append(value)
        if value > self.threshold:
            self.notify_alert(value)

    def subscribe(self, func):
        """Suscribe una función de alerta."""
        if func not in self.subscribers:
            self.subscribers.append(func)

    def notify_alert(self, value: float):
        """Notifica a todos los suscriptores de un valor de alerta."""
        for func in self.subscribers:
            func(value)

    def get_max_sensor(self) -> float:
        """Devuelve el valor máximo registrado en los sensores."""
        return max(self.sensors) if self.sensors else 0.0


# --- EJERCICIO 4: VersionedStorage ---
class VersionedStorage:
    def __init__(self):
        """Inicializa almacenamiento con versiones vacías."""
        self.versions = []  # lista de diccionarios

    def add_version(self, data: dict):
        """Agrega una nueva versión de datos."""
        self.versions.append(data.copy())

    def get_version(self, index: int) -> dict:
        """Obtiene versión específica (compatibilidad hacia atrás)."""
        if 0 <= index < len(self.versions):
            return self.versions[index].copy()
        return None

    def get_latest(self) -> dict:
        """Obtiene la última versión de datos."""
        return self.versions[-1].copy() if self.versions else None


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
    assert tasks == ["Email client", "Write report"]
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
    print("----- Simulacro ICA Industrial – Nivel 4 (Completo) -----")
    print("Tiempo sugerido: 90 minutos\n")
    test_employee_manager()
    test_task_scheduler()
    test_sensor_system()
    test_versioned_storage()
    print("\nTodos los tests completados ✅ ¡Simulacro listo!")
