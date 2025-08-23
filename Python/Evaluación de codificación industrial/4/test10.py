# =========================
# Simulacro ICA Industrial – Nivel 4 (Entry-Level)
# =========================
# Tiempo sugerido: 90 minutos
# Objetivo: Reutilización, refactorización y encapsulación.
# Nota: El Ejercicio 4 combina lo visto en los anteriores.

# --- EJERCICIO 1: EmployeeManager ---
# Enunciado:
# Crea una clase EmployeeManager que gestione empleados con nombre y salario.
# Debe permitir añadir, eliminar empleados, calcular salario promedio y
# obtener el empleado con mayor salario.

class EmployeeManager:
    def __init__(self):
        self.employees = []  # lista de diccionarios: {"name": str, "salary": float}

    def add_employee(self, name: str, salary: float):
        for emp in self.employees:
            if emp["name"] == name:
                emp["salary"] = salary
                return
        self.employees.append({"name": name, "salary": salary})

    def remove_employee(self, name: str):
        for emp in self.employees:
            if emp["name"] == name:
                self.employees.remove(emp)
                break

    def get_average_salary(self) -> float:
        if not self.employees:
            return None
        total = sum(emp["salary"] for emp in self.employees)
        return total / len(self.employees)

    def get_highest_salary(self) -> dict:
        if not self.employees:
            return None
        return max(self.employees, key=lambda e: e["salary"])


# --- EJERCICIO 2: TaskScheduler ---
# Enunciado:
# Crea una clase TaskScheduler que gestione tareas con prioridad.
# Debe permitir añadir tareas, obtener la siguiente más prioritaria
# y listar todas las tareas en orden descendente.

class TaskScheduler:
    def __init__(self):
        self.tasks = []  # lista de diccionarios: {"task": str, "priority": int}

    def add_task(self, task: str, priority: int):
        self.tasks.append({"task": task, "priority": priority})

    def get_next_task(self) -> str:
        if not self.tasks:
            return None
        highest = max(self.tasks, key=lambda t: t["priority"])
        self.tasks.remove(highest)
        return highest["task"]

    def get_all_tasks(self) -> list:
        sorted_tasks = sorted(self.tasks, key=lambda t: t["priority"], reverse=True)
        return [t["task"] for t in sorted_tasks]


# --- EJERCICIO 3: SensorSystem ---
# Enunciado:
# Implementa un sistema de sensores que notifique alertas si un valor supera un umbral.
# Permite suscribir funciones de alerta, agregar sensores y obtener el valor máximo.

class SensorSystem:
    def __init__(self, threshold: float):
        self.sensors = []        # lista de valores de sensores
        self.threshold = threshold
        self.subscribers = []    # funciones a notificar

    def add_sensor(self, value: float):
        self.sensors.append(value)
        if value > self.threshold:
            self.notify_alert(value)

    def subscribe(self, func):
        if func not in self.subscribers:
            self.subscribers.append(func)

    def notify_alert(self, value: float):
        for func in self.subscribers:
            func(value)

    def get_max_sensor(self) -> float:
        if not self.sensors:
            return None
        return max(self.sensors)


# --- EJERCICIO 4: CompanySystem (Integrador) ---
# Enunciado:
# Implementa una clase CompanySystem que integre los 3 sistemas anteriores:
# 1. Gestiona empleados con EmployeeManager.
# 2. Gestiona tareas con TaskScheduler.
# 3. Registra sensores críticos con SensorSystem.
#
# Métodos:
# - add_employee(name, salary)
# - assign_task(employee, task, priority)
# - record_sensor(value)
# - get_company_status() -> devuelve un dict con:
#       {"avg_salary": ..., "pending_tasks": [...], "max_sensor": ...}

class CompanySystem:
    def __init__(self, threshold: float):
        self.employees = EmployeeManager()
        self.tasks = TaskScheduler()
        self.sensors = SensorSystem(threshold)

    def add_employee(self, name: str, salary: float):
        self.employees.add_employee(name, salary)

    def assign_task(self, employee: str, task: str, priority: int):
        # Nota: simplificamos y solo añadimos la tarea (sin validar empleado).
        self.tasks.add_task(f"{employee}: {task}", priority)

    def record_sensor(self, value: float):
        self.sensors.add_sensor(value)

    def get_company_status(self) -> dict:
        return {
            "avg_salary": self.employees.get_average_salary(),
            "pending_tasks": self.tasks.get_all_tasks(),
            "max_sensor": self.sensors.get_max_sensor()
        }


# =========================
# TESTS DEL SIMULACRO
# =========================

def test_employee_manager():
    mgr = EmployeeManager()
    mgr.add_employee("Alice", 5000)
    mgr.add_employee("Bob", 6000)
    assert mgr.get_average_salary() == 5500
    assert mgr.get_highest_salary()["name"] == "Bob"
    mgr.remove_employee("Alice")
    assert len(mgr.employees) == 1
    print("EmployeeManager ✅")

def test_task_scheduler():
    scheduler = TaskScheduler()
    scheduler.add_task("Report", 2)
    scheduler.add_task("Fix bug", 5)
    assert scheduler.get_next_task() == "Fix bug"
    assert scheduler.get_all_tasks() == ["Report"]
    print("TaskScheduler ✅")

def test_sensor_system():
    alerts = []
    def alert_func(value): alerts.append(value)
    sensors = SensorSystem(threshold=10)
    sensors.subscribe(alert_func)
    sensors.add_sensor(8)
    sensors.add_sensor(15)
    assert sensors.get_max_sensor() == 15
    assert alerts == [15]
    print("SensorSystem ✅")

def test_company_system():
    company = CompanySystem(threshold=50)
    company.add_employee("Alice", 4000)
    company.add_employee("Bob", 6000)
    company.assign_task("Alice", "Prepare Report", 3)
    company.record_sensor(45)
    company.record_sensor(55)
    status = company.get_company_status()
    assert status["avg_salary"] == 5000
    assert "Alice: Prepare Report" in status["pending_tasks"]
    assert status["max_sensor"] == 55
    print("CompanySystem ✅")


# =========================
# MAIN
# =========================
if __name__ == "__main__":
    print("=== Simulacro ICA Industrial – Nivel 4 ===")
    test_employee_manager()
    test_task_scheduler()
    test_sensor_system()
    test_company_system()
    print("\n✅ Todos los tests pasaron – Simulacro completado")
