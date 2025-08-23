# =========================
# Simulacro ICA #2 – Código Listo
# =========================

# --- EJERCICIO 1: EmployeeManager ---
class EmployeeManager:
    def __init__(self):
        """Inicializa la lista de empleados vacía."""
        self.employees = []  # lista de diccionarios: {"name": str, "salary": float}

    def add_employee(self, name: str, salary: float):
        """Agrega un empleado al sistema."""
        pass

    def remove_employee(self, name: str):
        """Elimina un empleado por nombre si existe."""
        pass

    def get_average_salary(self) -> float:
        """Devuelve el salario promedio de todos los empleados, o None si no hay."""
        pass

    def get_highest_salary(self) -> dict:
        """Devuelve el empleado con salario más alto, o None si no hay."""
        pass


# --- EJERCICIO 2: TaskScheduler ---
class TaskScheduler:
    def __init__(self):
        """Inicializa la lista de tareas vacía."""
        self.tasks = []  # lista de diccionarios: {"task": str, "priority": int}

    def add_task(self, task: str, priority: int):
        """Agrega una tarea con prioridad. Prioridad más alta = más importante."""
        pass

    def get_next_task(self) -> str:
        """Devuelve la tarea más prioritaria y la elimina de la lista."""
        pass

    def get_all_tasks(self) -> list:
        """Devuelve todas las tareas ordenadas por prioridad descendente."""
        pass


# --- EJERCICIO 3: SensorSystem (Observer Pattern) ---
class SensorSystem:
    def __init__(self, threshold: float):
        """Inicializa sistema de sensores con un umbral de alerta."""
        self.sensors = []  # lista de valores de sensores
        self.threshold = threshold
        self.subscribers = []  # funciones que se llaman cuando hay alerta

    def add_sensor(self, value: float):
        """Agrega una lectura de sensor y notifica si supera el umbral."""
        pass

    def subscribe(self, func):
        """Suscribe una función que será llamada en caso de alerta."""
        pass

    def notify_alert(self, value: float):
        """Llama a todas las funciones suscritas con el valor de alerta."""
        pass

    def get_max_sensor(self) -> float:
        """Devuelve la lectura máxima actual, o None si no hay sensores."""
        pass


# =========================
# TESTS DEL SIMULACRO
# =========================

def test_employee_manager():
    mgr = EmployeeManager()
    mgr.add_employee("Alice", 5000)
    mgr.add_employee("Bob", 6000)
    mgr.add_employee("Charlie", 5500)

    assert mgr.get_average_salary() == (5000 + 6000 + 5500) / 3
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


# =========================
# EJECUCIÓN DE TESTS
# =========================

if __name__ == "__main__":
    print("----- Simulacro ICA #2 -----")
    print("Tiempo sugerido: 90 minutos para completarlo.\n")

    test_employee_manager()
    test_task_scheduler()
    test_sensor_system()

    print("\nTodos los tests completados ✅ ¡Simulacro listo!")
