# =========================
# Simulacro ICA #3 – Borrador
# =========================

# --- EJERCICIO 1: InventoryManager ---
class InventoryManager:
    def __init__(self):
        """Inicializa un inventario vacío."""
        self.items = {}  # {nombre: cantidad}

    def add_item(self, name: str, quantity: int):
        """Agrega una cantidad al inventario, o crea el item si no existe."""
        pass

    def remove_item(self, name: str, quantity: int):
        """Remueve cantidad del inventario, no permite negativas."""
        pass

    def get_total_items(self) -> int:
        """Devuelve el total de tipos de items en inventario."""
        pass


# --- EJERCICIO 2: BankAccount (Encapsulación) ---
class BankAccount:
    def __init__(self, owner: str, balance: float = 0):
        """Inicializa la cuenta bancaria con dueño y balance inicial."""
        self.owner = owner
        self.__balance = balance  # atributo privado

    def deposit(self, amount: float):
        """Deposita una cantidad positiva."""
        pass

    def withdraw(self, amount: float):
        """Retira una cantidad si hay saldo suficiente."""
        pass

    def get_balance(self) -> float:
        """Devuelve el balance actual."""
        pass


# --- EJERCICIO 3: Logger (Singleton Pattern) ---
class Logger:
    __instance = None

    def __new__(cls):
        """Garantiza que solo exista una instancia."""
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__instance.logs = []
        return cls.__instance

    def log(self, message: str):
        """Agrega un mensaje al registro de logs."""
        pass

    def get_logs(self):
        """Devuelve la lista de logs."""
        pass


# --- EJERCICIO 4: NotificationCenter (Observer Pattern) ---
class NotificationCenter:
    def __init__(self):
        self.subscribers = []

    def subscribe(self, func):
        """Suscribe una función a las notificaciones."""
        pass

    def notify(self, message: str):
        """Notifica a todos los suscriptores con un mensaje."""
        pass


# =========================
# TESTS DEL SIMULACRO
# =========================

def test_inventory_manager():
    inv = InventoryManager()
    inv.add_item("apple", 10)
    inv.add_item("banana", 5)
    inv.add_item("apple", 3)
    assert inv.get_total_items() == 2
    inv.remove_item("banana", 2)
    inv.remove_item("banana", 5)
    print("InventoryManager tests listos ✅")


def test_bank_account():
    acc = BankAccount("Alice", 100)
    acc.deposit(50)
    acc.withdraw(70)
    print("BankAccount tests listos ✅")


def test_logger():
    logger1 = Logger()
    logger2 = Logger()
    logger1.log("Start")
    logger2.log("Process")
    print("Logger tests listos ✅")


def test_notification_center():
    messages = []

    def subscriber(msg):
        messages.append(msg)

    nc = NotificationCenter()
    nc.subscribe(subscriber)
    nc.notify("Hello")
    print("NotificationCenter tests listos ✅")


# =========================
# EJECUCIÓN DE TESTS
# =========================

if __name__ == "__main__":
    print("----- Simulacro ICA #3 (Borrador) -----")
    print("Tiempo sugerido: 90 minutos para completarlo.\n")

    test_inventory_manager()
    test_bank_account()
    test_logger()
    test_notification_center()

    print("\nTests de borrador listos ✅ ¡Completa los métodos!")
