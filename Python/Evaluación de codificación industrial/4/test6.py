# =========================
# EJERCICIO 1 – LibraryManager
# =========================
# Crea una clase que administre libros en una biblioteca:
# - Permite agregar libros con título y autor
# - Permite eliminar un libro por título
# - Permite devolver la lista de todos los libros

class LibraryManager:
    def __init__(self):
        """Inicializa la lista de libros vacía."""
        self.books = []

    def add_book(self, title, author):
        """Agrega un libro con su título y autor."""
        self.books.append({"title": title, "author": author})

    def remove_book(self, title):
        """Elimina un libro por título si existe."""
        for b in self.books:
            if b["title"] == title:
                self.books.remove(b)
                break

    def get_all_books(self):
        """Devuelve la lista de todos los títulos de libros."""
        return [b["title"] for b in self.books]


# =========================
# EJERCICIO 2 – TicketSystem
# =========================
# Crea una clase que maneje tickets de soporte:
# - Cada ticket tiene un ID y nivel de prioridad (1-5, 5 = más urgente)
# - Permite agregar tickets
# - Permite sacar el ticket más urgente
# - Permite devolver todos los tickets ordenados por prioridad descendente

class TicketSystem:
    def __init__(self):
        self.tickets = []

    def add_ticket(self, ticket_id, priority):
        """Agrega un ticket con ID y prioridad."""
        self.tickets.append({"id": ticket_id, "priority": priority})

    def get_next_ticket(self):
        """Devuelve el ID del ticket con mayor prioridad y lo elimina."""
        if not self.tickets:
            return None
        highest = self.tickets[0]
        for t in self.tickets:
            if t["priority"] > highest["priority"]:
                highest = t
        self.tickets.remove(highest)
        return highest["id"]

    def get_all_tickets(self):
        """Devuelve todos los IDs de tickets ordenados por prioridad descendente."""
        sorted_tickets = sorted(self.tickets, key=lambda t: t["priority"], reverse=True)
        return [t["id"] for t in sorted_tickets]


# =========================
# EJERCICIO 3 – AlertSystem (Observer Pattern)
# =========================
# Crea una clase que registre valores y alerte a funciones suscritas si se supera un límite:
# - Permite agregar lecturas
# - Permite suscribirse a alertas
# - Notifica a todas las funciones suscritas si la lectura supera el límite

class AlertSystem:
    def __init__(self, limit):
        self.readings = []
        self.limit = limit
        self.subscribers = []

    def add_reading(self, value):
        """Agrega una lectura y notifica si supera el límite."""
        self.readings.append(value)
        if value > self.limit:
            self.notify_alert(value)

    def subscribe(self, func):
        """Suscribe una función que será llamada si hay alerta."""
        if func not in self.subscribers:
            self.subscribers.append(func)

    def notify_alert(self, value):
        """Notifica a todas las funciones suscritas."""
        for func in self.subscribers:
            func(value)


# =========================
# EJERCICIO 4 – EmployeeTracker
# =========================
# Crea una clase que administre empleados activos:
# - Permite agregar empleados con nombre
# - Permite desactivar empleados
# - Permite devolver la lista de empleados activos

class EmployeeTracker:
    def __init__(self):
        self.employees = []

    def add_employee(self, name):
        """Agrega un empleado como activo si no existe."""
        for e in self.employees:
            if e["name"] == name:
                return
        self.employees.append({"name": name, "active": True})

    def deactivate_employee(self, name):
        """Desactiva un empleado por nombre."""
        for e in self.employees:
            if e["name"] == name:
                e["active"] = False

    def get_active_employees(self):
        """Devuelve la lista de empleados activos."""
        return [e["name"] for e in self.employees if e["active"]]


# =========================
# TESTS
# =========================

def test_library_manager():
    lib = LibraryManager()
    lib.add_book("Book1", "AuthorA")
    lib.add_book("Book2", "AuthorB")
    lib.remove_book("Book1")
    assert lib.get_all_books() == ["Book2"]
    print("LibraryManager passed ✅")


def test_ticket_system():
    ts = TicketSystem()
    ts.add_ticket(1, 3)
    ts.add_ticket(2, 5)
    ts.add_ticket(3, 2)
    assert ts.get_next_ticket() == 2
    assert ts.get_all_tickets() == [1, 3]
    print("TicketSystem passed ✅")


def test_alert_system():
    triggered = []
    def alert_func(val):
        triggered.append(val)
    a = AlertSystem(limit=50)
    a.subscribe(alert_func)
    a.add_reading(45)
    a.add_reading(55)
    assert triggered == [55]
    print("AlertSystem passed ✅")


def test_employee_tracker():
    et = EmployeeTracker()
    et.add_employee("Alice")
    et.add_employee("Bob")
    et.deactivate_employee("Bob")
    assert et.get_active_employees() == ["Alice"]
    print("EmployeeTracker passed ✅")


# =========================
# EJECUCIÓN DE TESTS
# =========================

if __name__ == "__main__":
    test_library_manager()
    test_ticket_system()
    test_alert_system()
    test_employee_tracker()
    print("\nTodos los tests completados ✅ Examen listo")
