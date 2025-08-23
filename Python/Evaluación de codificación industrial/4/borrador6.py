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
        pass  # <-- Completar

    def remove_book(self, title):
        """Elimina un libro por título si existe."""
        pass  # <-- Completar

    def get_all_books(self):
        """Devuelve la lista de todos los títulos de libros."""
        pass  # <-- Completar


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
        pass  # <-- Completar

    def get_next_ticket(self):
        """Devuelve el ID del ticket con mayor prioridad y lo elimina."""
        pass  # <-- Completar

    def get_all_tickets(self):
        """Devuelve todos los IDs de tickets ordenados por prioridad descendente."""
        pass  # <-- Completar


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
        pass  # <-- Completar

    def subscribe(self, func):
        """Suscribe una función que será llamada si hay alerta."""
        pass  # <-- Completar

    def notify_alert(self, value):
        """Notifica a todas las funciones suscritas."""
        pass  # <-- Completar


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
        pass  # <-- Completar

    def deactivate_employee(self, name):
        """Desactiva un empleado por nombre."""
        pass  # <-- Completar

    def get_active_employees(self):
        """Devuelve la lista de empleados activos."""
        pass  # <-- Completar
